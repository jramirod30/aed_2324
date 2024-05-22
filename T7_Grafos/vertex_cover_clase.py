import copy
from typing import TypeVar, Set, Iterator

from tads import IUndirectedGraph, UndirectedAdjacencyListGraph, Vertex, Edge

V = TypeVar('V')
E = TypeVar('E')

grafo2: IUndirectedGraph[int, int] = UndirectedAdjacencyListGraph()

v1: Vertex[int] = grafo2.insert_vertex(1)
v2: Vertex[int] = grafo2.insert_vertex(2)
v3: Vertex[int] = grafo2.insert_vertex(3)
v4: Vertex[int] = grafo2.insert_vertex(4)
v5: Vertex[int] = grafo2.insert_vertex(5)
v6: Vertex[int] = grafo2.insert_vertex(6)
v7: Vertex[int] = grafo2.insert_vertex(7)
v8: Vertex[int] = grafo2.insert_vertex(8)
v9: Vertex[int] = grafo2.insert_vertex(9)

grafo2.insert_edge(v1, v2, 1)
grafo2.insert_edge(v1, v3, 1)
grafo2.insert_edge(v1, v4, 1)
grafo2.insert_edge(v1, v5, 1)
grafo2.insert_edge(v1, v6, 1)
grafo2.insert_edge(v1, v7, 1)
grafo2.insert_edge(v1, v8, 1)
grafo2.insert_edge(v1, v9, 1)
grafo2.insert_edge(v2, v3, 1)
grafo2.insert_edge(v2, v4, 1)
grafo2.insert_edge(v2, v5, 1)
grafo2.insert_edge(v3, v6, 1)
grafo2.insert_edge(v3, v8, 1)
grafo2.insert_edge(v4, v6, 1)
grafo2.insert_edge(v4, v8, 1)
grafo2.insert_edge(v5, v6, 1)


def vertex_cover(udg: IUndirectedGraph[V, E]) -> Set[Vertex[V]]:
    udg1: IUndirectedGraph[V, E] = copy.deepcopy(udg)
    result: Set[Vertex[V]] = set()
    # TO-DO
    while udg1.num_edges() > 0:
        edges: Iterator[Edge[V, E]] = udg1.edges()
        edge: Edge[V, E] = next(edges, None)
        u: Vertex[V] = edge.endpoints()[0]
        v: Vertex[V] = edge.endpoints()[1]
        udg1.remove_vertex(v)
        udg1.remove_vertex(u)
        result |= {v, u}
    return result


print([v.element for v in vertex_cover(grafo2)])
