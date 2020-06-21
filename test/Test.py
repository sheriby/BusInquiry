#! /usr/bin/python3

from Vertex import Vertex
from Graph import Graph

if __name__ == "__main__":
    vertex = Vertex(1)
    graph = Graph()
    graph.addVertex(1)
    graph.addVertex(2)
    graph.addVertex(3)
    graph.addVertex(4)
    graph.addVertex(5)
    graph.addVertex(6)
    graph.addVertex(7)
    graph.addVertex(8)
    graph.addVertex(9)

    graph.addEdge(1, 3, 1, 0)
    graph.addEdge(3, 6, 1, 0)
    graph.addEdge(6, 9, 1, 0)
    graph.addEdge(4, 5, 2, 0)
    graph.addEdge(5, 6, 2, 0)
    graph.addEdge(6, 7, 2, 0)
    graph.addEdge(2, 3, 3, 0)
    graph.addEdge(3, 5, 3, 0)
    graph.addEdge(5, 8, 3, 0)

    print(graph.getVertexs())
    graph.getBus(1, 1)
    graph.getBus(2, 4)
    graph.getBus(3, 2)
