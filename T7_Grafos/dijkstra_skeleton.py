import sys, copy
from typing import TypeVar, List, Iterator, Set, Dict, Optional

from tads.graph import UndirectedAdjacencyListGraph
from tads.graph.elements import Vertex, Edge
from tads.graph.iundirected_graph import IUndirectedGraph

V = TypeVar('V')
E = TypeVar('E')

grafo: IUndirectedGraph[int, int] = UndirectedAdjacencyListGraph()

v1: Vertex[int] = grafo.insert_vertex(1)
v2: Vertex[int] = grafo.insert_vertex(2)
v3: Vertex[int] = grafo.insert_vertex(3)
v4: Vertex[int] = grafo.insert_vertex(4)
v5: Vertex[int] = grafo.insert_vertex(5)
v6: Vertex[int] = grafo.insert_vertex(6)

a12: Edge[int, int] = grafo.insert_edge(v1, v2, 100)
grafo.insert_edge(v1, v3, 400)
grafo.insert_edge(v1, v4, 600)
grafo.insert_edge(v2, v3, 200)
grafo.insert_edge(v3, v4, 300)
grafo.insert_edge(v3, v6, 500)

"""
    1   2   3   4   5   6
1       100 400 600
2   100     200
3   400 200     300     500
4   600     300
5
6           500
"""


def dijkstra(udg: IUndirectedGraph[V, E], org: Vertex[V]) -> (Dict[Vertex[V], int], Dict[Vertex[V], Vertex[V]]):
    distances: Dict[Vertex[V], int] = {}
    prev: Dict[Vertex[V], Vertex[V]] = {}
    unvisited: Set[Vertex[V]] = set()
    # initialize weights to inf except for the origin
    for vertex in udg.vertices():
        distances[vertex] = sys.maxsize
        unvisited.add(vertex)
    distances[org] = 0
    # TODO: Update the minimum distances and the previous vertex
    return distances, prev


def min_dist(distances: Dict[Vertex[V], int], unvisited: Set[Vertex[V]]) -> Vertex[V]:
    min_v: Optional[Vertex[V]] = None
    # TODO: return the vertex with the minimum distance
    return min_v
