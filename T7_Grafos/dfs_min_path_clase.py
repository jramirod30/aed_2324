import sys
from typing import TypeVar, List, Set, Iterator, Tuple, Optional

from tads import IDirectedGraph, Edge
from tads.graph import DirectedAdjacencyListGraph
from tads.graph.elements import Vertex

V = TypeVar('V')
E = TypeVar('E')

g: IDirectedGraph[int, int] = DirectedAdjacencyListGraph()
v1 = g.insert_vertex(1)
v2 = g.insert_vertex(2)
v3 = g.insert_vertex(3)
v4 = g.insert_vertex(4)
v5 = g.insert_vertex(5)
v6 = g.insert_vertex(6)

e1 = g.insert_edge(v1, v2, 7)
g.insert_edge(v2, v1, 7)
g.insert_edge(v1, v3, 9)
g.insert_edge(v3, v1, 9)
g.insert_edge(v1, v6, 14)
g.insert_edge(v6, v1, 14)
g.insert_edge(v2, v3, 10)
g.insert_edge(v3, v2, 10)
g.insert_edge(v2, v4, 15)
g.insert_edge(v4, v2, 15)
g.insert_edge(v3, v4, 11)
g.insert_edge(v4, v3, 11)
g.insert_edge(v3, v6, 2)
g.insert_edge(v6, v3, 2)
g.insert_edge(v4, v5, 6)
g.insert_edge(v5, v4, 6)
g.insert_edge(v5, v6, 9)
g.insert_edge(v6, v5, 9)

print(g)


def get_neighbors(gf: IDirectedGraph[V, E], org) -> List[Vertex[V]]:
    result: List[Vertex[V]] = []
    node: Vertex[V]
    edge: Edge[V, E]
    for edge in gf.outgoing_edges(org):
        node = edge.opposite(org)
        result.append(node)
    return result


def filter_visited(all: List[Vertex[V]], visited: Set[Vertex[V]]) -> List[Vertex[V]]:
    return [v for v in all if v not in visited]


def get_cost(udg: IDirectedGraph[V, E], org: Vertex[V], target: Vertex[V]) -> int:
    """
    PRE: edge (org, target) in udg

    POST: return the weight of the edge (org, target) in udg
    """
    edges: Iterator[Edge[V, E]] = udg.outgoing_edges(org)
    edge: Edge[E, V] = next(edges, None)
    while edge is not None and edge.opposite(org) != target:
        edge = next(edges, None)
    return edge.element


def find_min_path(udg: IDirectedGraph[V, E], org: Vertex[V], target: Vertex[V]) -> \
    Tuple[List[Vertex[V]], int]:
    pass  # TO-DO


print([v.element for v in get_neighbors(g, v1)])