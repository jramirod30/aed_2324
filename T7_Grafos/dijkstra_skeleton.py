import sys
from typing import Dict, Set, TypeVar, Optional, List, Iterator

from tads import IUndirectedGraph, Vertex, Edge, UndirectedAdjacencyListGraph

V = TypeVar('V')
E = TypeVar('E')

grafo: IUndirectedGraph[int, int] = UndirectedAdjacencyListGraph()

v1: Vertex[int] = grafo.insert_vertex(1)
v2: Vertex[int] = grafo.insert_vertex(2)
v3: Vertex[int] = grafo.insert_vertex(3)
v4: Vertex[int] = grafo.insert_vertex(4)
v5: Vertex[int] = grafo.insert_vertex(5)
v6: Vertex[int] = grafo.insert_vertex(6)

e1 = grafo.insert_edge(v1, v2, 7)
grafo.insert_edge(v1, v3, 9)
grafo.insert_edge(v1, v6, 14)
grafo.insert_edge(v2, v3, 10)
grafo.insert_edge(v2, v4, 15)
grafo.insert_edge(v3, v4, 11)
grafo.insert_edge(v3, v6, 2)
grafo.insert_edge(v4, v5, 6)
grafo.insert_edge(v5, v6, 9)

"""
    1   2   3   4   5   6
1       100 400 600
2   100     200
3   400 200     300     500
4   600     300
5
6           500
"""


def get_neighbors(gf: IUndirectedGraph[V, E], org: Vertex[V]) -> List[Vertex[V]]:
    result: List[Vertex[V]] = []
    for edge in gf.edges_of(org):
        node = edge.opposite(org)
        result.append(node)
    return result


def get_cost(udg: IUndirectedGraph[V, E], org: Vertex[V], target: Vertex[V]) -> int:
    """
    PRE: edge (org, target) in udg

    POST: return the weight of the edge (org, target) in udg
    """
    edges: Iterator[Edge[V, E]] = udg.edges_of(org)
    edge: Edge[E, V] = next(edges, None)
    while edge is not None and edge.opposite(org) != target:
        edge = next(edges, None)
    return edge.element


def dijkstra(udg: IUndirectedGraph[V, E], org: Vertex[V]) -> (Dict[Vertex[V], int], Dict[Vertex[V], Vertex[V]]):
    distances: Dict[Vertex[V], int] = {}
    prev: Dict[Vertex[V], Vertex[V]] = {}
    unvisited: Set[Vertex[V]] = set()
    # initialize weights to inf except for the origin
    for vertex in udg.vertices():
        distances[vertex] = sys.maxsize
        unvisited.add(vertex)
    distances[org] = 0

    while len(unvisited) > 0:
        a: Vertex[V] = min_dist(distances, unvisited)
        neighbors = get_neighbors(udg, a)
        for neighbor in neighbors:
            if neighbor in unvisited:
                dt = distances[a] + get_cost(udg, a, neighbor)
                if dt < distances[neighbor]:
                    distances[neighbor] = dt
                    prev[neighbor] = a
        unvisited.remove(a)
    return distances, prev


def min_dist(distances: Dict[Vertex[V], int], unvisited: Set[Vertex[V]]) -> Vertex[V]:
    min_v: Optional[Vertex[V]] = None
    dist_min: int = sys.maxsize
    for a in unvisited:
        if distances[a] < dist_min:
            min_v = a
            dist_min = distances[a]
    return min_v


def build_path(org: Vertex[V], target: Vertex[V],
               visited_vertices: Dict[Vertex[V], Vertex[V]]) -> (
        List)[Vertex[V]]:
    if org == target:
        return [org]
    else:
        path: List[Vertex[V]] = build_path(org,
                                           visited_vertices[target],
                                           visited_vertices)
        path.append(target)
        return path


distances, prev = dijkstra(grafo, v1)
print([(v.element, distances[v]) for v in distances.keys()])
print([(v.element, prev[v].element) for v in prev.keys()])

print([v.element for v in build_path(v1, v5, prev)])
