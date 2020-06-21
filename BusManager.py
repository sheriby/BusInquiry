from Graph import Graph
import json
import redis


class BusManager(object):
    def __init__(self):
        super().__init__()
        self.graph = Graph()
        self.busName2IdMap = {}
        self.busId2NameMap = {}
        self.busStart = {}
        self.id = 1

        # self.loadJson('BusInquiry/buses.json')
        self.getDataFromRedis()

    def loadJson(self, jsonfileName):
        with open(jsonfileName, 'r') as f:
            buses = json.load(f)
        for k, v in buses.items():
            self.addBusRoute(int(k), v['route'], v['distance'])

    def genBusNameId(self, route: list):
        for i in range(len(route)):
            name = route[i]
            if name not in self.busName2IdMap:
                self.busId2NameMap[self.id] = name
                self.busName2IdMap[name] = self.id
                self.id += 1
            route[i] = self.busName2IdMap[route[i]]
        # print(route)

    def addBusRoute(self, num: int, route: list, weight: list):
        self.genBusNameId(route)
        for i in range(len(route)-1):
            self.graph.addEdge(route[i], route[i+1], num, weight[i])
        self.busStart[str(num)] = route[0]

    def queryBusRoute(self, num) -> list:
        if str(num) not in self.busStart:
            return None
        result = self.graph.getBus(num, self.busStart[str(num)])
        return result

    def deleteBusRoute(self, num: int) -> bool:
        if str(num) not in self.busStart:
            return False
        route = self.graph.getBus(num, self.busStart[str(num)])
        del self.busStart[str(num)]
        for i in range(len(route) - 1):
            res = self.graph.deleteEdge(route[i], route[i+1], num)
            if res != None and res > 0:
                self.delOneVertexMap(route[i])
                if res > 1:
                    self.delOneVertexMap(route[i+1])

        return True

    def delOneVertexMap(self, busid):
        name = self.busId2NameMap[busid]
        del self.busId2NameMap[busid]
        del self.busName2IdMap[name]

    def selectBusRoute(self, start, end):
        routes = self.graph.dfs(start, end)
        minBus = self.minBusRoute(routes)
        minDis = self.minDistanceRoute(routes)
        return (self.displayRoute(minBus), self.displayRoute(minDis))

    def minBusRoute(self, routes: list) -> list:
        busLists = []
        busDisList = []

        for n in range(len(routes)):
            busList = []
            eachBus = []
            curBus = -1
            busNum = 1
            route = routes[n]

            for i in range(len(route) - 1):
                startVertex = self.graph.vertexLists[route[i]]
                bus = startVertex.getBus(route[i+1])

                if curBus == -1:
                    curBus = bus
                    eachBus.append(curBus)
                    continue

                tmp = [x for x in bus if x in curBus]
                if tmp == []:
                    curBus = bus
                    busNum += 1
                    eachBus.append(curBus)
                else:
                    curBus = tmp
                    eachBus.append(curBus)

            busList.append(n)
            busList.append(busNum)
            busList.append(eachBus)
            busLists.append(busList)

        busLists.sort(key=lambda x: x[1])
        minBusLists = []
        for busList in busLists:
            if minBusLists == []:
                minBusLists.append(busList)
                continue
            if busList[1] == minBusLists[0][1]:
                minBusLists.append(busList)

        minIndex = 0
        minValue = self.getRouteDistance(routes[minBusLists[0][0]])

        if len(minBusLists) == 1:
            minBusLists = minBusLists[0]
        else:
            i = 1
            while i < len(minBusLists):
                value = self.getRouteDistance(routes[minBusLists[i][0]])
                if value < minValue:
                    minValue = value
                    minIndex = i
                i += 1

        minBusLists = busLists[minIndex]
        minbusRoute = routes[minBusLists[0]]
        return (minbusRoute, self.simplyRoute(minBusLists[2]), minValue)

    def simplyRoute(self, route: list):
        i = 0
        j = 1
        while j < len(route):
            listi = route[i]
            listj = route[j]
            if listi == listj:
                j += 1
            elif listi != listj:
                tmp = [x for x in listi if x in listj]
                if tmp == []:
                    i = j
                else:
                    k = i
                    while k <= j:
                        route[k] = tmp
                        k += 1
                j += 1
        return route

    def minDistanceRoute(self, routes: list) -> list:
        for i in range(len(routes)):
            route = routes[i]
            distance = self.getRouteDistance(route)
            routes[i] = (distance, route)
        routes.sort(key=lambda x: x[0])
        minBus = self.minBusRoute([routes[0][1]])
        return minBus

    def getRouteDistance(self, route: list) -> int:
        distance = 0
        for i in range(len(route) - 1):
            distance += self.graph.getNbrWeight(route[i], route[i+1])
        return distance

    def printRoute(self, route: list):
        for busid in route[0:-1]:
            print(self.busId2NameMap[busid], '->', end=' ')
        print(self.busId2NameMap[route[-1]])

    def getRouteName(self, route: list) -> list:
        return list(map(lambda x: self.busId2NameMap[x], route))

    def displayRoute(self, route) -> str:
        '''
        route is (stopList, busList, distance) such as:
        ([53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 15,
         14, 13, 12, 11, 10, 9, 1, 7, 6, 63, 64, 65, 66, 67, 68, 69, 70],
         [[4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], 
         [4], [4], [22], [22], [22], [22], [22], [22], [22], [22], [22], [22], [22], [22],
          [22], [22], [22], [22], [22]],
          109)
        '''
        display = ''
        stopList = route[0]
        busLists = route[1]
        distance = route[2]

        curBus = busLists[0]
        display += self.displayAStop(busLists[0])
        display += self.busId2NameMap[stopList[0]]

        for i in range(1, len(stopList)):
            display += ' => '
            display += self.busId2NameMap[stopList[i]]
            if i != len(stopList) - 1:
                bus = busLists[i]
                if bus != curBus:
                    curBus = bus
                    display += '\n'
                    display += self.displayAStop(bus)
        display += '  距离: %d' % distance
        return display

    def displayAStop(self, busList) -> str:
        if busList is None or len(busList) == 0:
            return ''
        if len(busList) == 1:
            return ' *(乘坐%d路) ' % busList[0]

        display = ' *(乘坐%d路' % busList[0]
        i = 1
        while i < len(busList):
            display += '或%d路' % busList[i]
            i += 1
        return display+') '

    def getWeightFromRoute(self, route: list) -> list:
        distance = []
        for i in range(len(route)-1):
            distance.append(self.graph.getNbrWeight(route[i], route[i+1]))
        return distance

    def getAllRouteAndWeight(self) -> [(int, list, list)]:
        results = []
        for busNum, start in self.busStart.items():
            route = self.graph.getBus(int(busNum), start)
            distance = self.getWeightFromRoute(route)
            results.append((busNum, route, distance))
        return results

    def getAllRouteAndWeightJson(self) -> str:
        results = self.getAllRouteAndWeight()
        jsonStr = '{'
        for result in results:
            jsonStr += '"%s":{"route":' % result[0]
            jsonStr += str(self.getRouteName(result[1]))
            jsonStr += ',"distance":'
            jsonStr += str(result[2])
            jsonStr += '},'
        jsonStr = jsonStr[0:-1] + '}'
        return jsonStr.replace("'", '"')

    def writeDataIntoRedis(self):
        results = self.getAllRouteAndWeight()
        r = redis.StrictRedis(host='localhost', port=6379, db=0)
        for i, result in enumerate(results):
            r.set('bus:id:%d' % i, str(result[0]))
            r.set('bus:data:%s:route' % result[0], str(
                self.getRouteName(result[1])))
            r.set('bus:data:%s:distance' % result[0], str(result[2]))

    def getDataFromRedis(self):
        r = redis.StrictRedis(host='localhost', port=6379, db=0)
        i = 0
        while True:
            busNum = r.get('bus:id:%d' % i)
            if busNum is None:
                break
            busNum = int(busNum)
            route = eval(r.get('bus:data:%d:route' % busNum))
            distance = eval(r.get('bus:data:%d:distance' % busNum))

            i += 1
            self.addBusRoute(busNum, route, distance)


if __name__ == "__main__":
    busManager = BusManager()
    # results = busManager.getAllRouteAndWeight()
    # print(results)
    results = busManager.getAllRouteAndWeightJson()
    print(results)
    # busManager.addBusRoute(2, ['a', 'b', 'c', '富丽花园站'], [1, 2, 3])
    # res1 = busManager.graph.getBus(1, busManager.buses['1']['route'][0])
    # print(res1)
    # res2 = busManager.graph.getBus(4, busManager.buses['4']['route'][0])
    # print(res2)
    # res3 = busManager.graph.getBus(22, busManager.buses['22']['route'][0])
    # print(res3)
    # busManager.addBusRoute(2, ['a', 'b', 'c'], [1, 2])
    # res4 = busManager.graph.getBus(2, busManager.busStart['2'])
    # print(res4)

    # busManager.deleteBusRoute(4)
    # busmanager.graph.getbus(2, buses[2][0])
    # busmanager.graph.getbus(3, buses[3][0])
    # busmanager.graph.getbus(1, buses[1][0])
    # results = busManager.selectBusRoute(
    #     busManager.busName2IdMap['a'], busManager.busName2IdMap['淮安信息学院站'])
    # print(results)
    # busManager.busName2IdMap['海口路站'], busManager.busName2IdMap['淮安信息学院站'])
    # for res in results:
    # busManager.printRoute(res)
    # print(results)
    # busManager.printRoute(results[0][0])
    # busManager.printRoute(results[1][0])
    # res = busManager.minBusRoute(results)
    # print(res)
    # busManager.printRoute(res[0])
    # res1 = busManager.minDistanceRoute(results)
    # print(res1)
    # busManager.printRoute(res1[0])
