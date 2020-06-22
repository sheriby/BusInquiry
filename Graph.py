'''
    The Graph of the bus route
'''

from Vertex import Vertex


class Graph(object):
    def __init__(self):
        self.vertexLists = {}
        self.numVertexs = 0

    def addVertex(self, id):
        if id in self.vertexLists:
            return None

        self.numVertexs += 1
        newVertex = Vertex(id)
        self.vertexLists[id] = newVertex

        return newVertex

    def getVertex(self, id):
        if id in self.vertexLists:
            return self.vertexLists[id]
        else:
            return None

    def __contains__(self, id):
        return id in self.vertexLists

    def addEdge(self, start: int, end: int, bus: int, weight: int):
        if start not in self.vertexLists:
            startVertex = self.addVertex(start)
        else:
            startVertex = self.vertexLists[start]
        if end not in self.vertexLists:
            endVertex = self.addVertex(end)
        else:
            endVertex = self.vertexLists[end]

        if startVertex.isNeighbor(end):
            startVertex.connectTo[end][0].append(bus)
            endVertex.connectTo[start][0].append(bus)
        else:
            startVertex.addNeighbor(end, bus, weight)
            endVertex.addNeighbor(start, bus, weight)

    def deleteEdge(self, start, end, bus):
        startVertex = self.vertexLists[start]
        endVertex = self.vertexLists[end]
        if end not in startVertex.connectTo:
            return None
        if bus not in startVertex.getBus(end):
            return None

        res = 0
        if len(startVertex.connectTo) == 1 and len(startVertex.getBus(end)) == 1:
            del startVertex
            del endVertex.connectTo[start]
            res += 1
        else:
            startVertex.connectTo[end][0].remove(bus)
            endVertex.connectTo[start][0].remove(bus)
            if len(endVertex.getBus(start)) == 0:
                del endVertex.connectTo[start]
        if len(endVertex.connectTo) == 0:
            del self.vertexLists[end]
            res += 1
        return res

    def getVertexs(self) -> list:
        return self.vertexLists.keys()

    def getNbrWeight(self, start: int, end: int):
        if start not in self.vertexLists or end not in self.vertexLists:
            return None
        startVertex = self.vertexLists[start]
        return startVertex.getWeight(end)

    def dfs(self, start, end):
        result = []
        visit = [start]
        self.dfsSearch(start, end, result, visit)
        return result

    def dfsSearch(self, start, end, result: list, visit: list):
        for vertex in self.vertexLists[start].connectTo:
            if vertex in visit:
                continue

            visit.append(vertex)

            if vertex == end:
                result.append(visit)
                return None

            self.dfsSearch(vertex, end, result, list(visit))
            visit.pop()
