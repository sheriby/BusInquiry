'''
    Vertex is the bus stop here.
'''


class Vertex(object):
    def __init__(self, id):
        self.id = id
        self.connectTo = {}

    def addNeighbor(self, nbr: int, bus: int, weight: int):
        if nbr not in self.connectTo:
            busList = []
        else:
            busList = self.connectTo[nbr][0]
        busList.append(bus)
        self.connectTo[nbr] = (busList, weight)

    def getConnection(self):
        return self.connectTo.keys()

    def getId(self):
        return self.id

    def getBus(self, nbr) -> list:
        if nbr in self.connectTo:
            return self.connectTo[nbr][0]
        else:
            return None

    def getWeight(self, nbr) -> int:
        if nbr in self.connectTo:
            return self.connectTo[nbr][1]
        else:
            return None

    def isNeighbor(self, id) -> bool:
        return id in self.connectTo

    def __str__(self):
        return str(self.id) + ' ConnectTo ' + str([x for x in self.connectTo])
