from typing import TypeVar, List, Iterator, Set, Dict, Optional, Any

from tads import IUndirectedGraph
from tads.graph import UndirectedAdjacencyListGraph
from tads.graph.elements import Vertex, Edge

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

print(grafo)

# print(a12.endpoints()[0].var)

def get_neighbours(udg: IUndirectedGraph[V, E], org: Vertex[V]) -> List[Vertex[V]]:
    # return [udg.opposite(org, edge) for edge in udg.edges_of(org)]
    result: List[Vertex[V]] = []
    for edge in udg.edges_of(org):
        result += [udg.opposite(org, edge)]
    return result

print([v.element for v in get_neighbours(grafo, v1)])

def find_path_dfs(udg: IUndirectedGraph[V, E], org: Vertex[V], obj: Vertex[V]) -> List[Vertex[V]]:
    """
    PRE: udg is not empty

    POST: returns the path from org to obj.
    """
    return find_path_aux(udg, org, obj, {org})


def find_path_aux(udg: IUndirectedGraph[V, E], org: Vertex[V],
                  obj: Vertex[V], visited: Set[Vertex[V]]) \
        -> List[Vertex[V]]:
    if org == obj:
        return [org]
    not_visited: List[Vertex[V]] = filter_visited(get_neighbours(udg, org), visited)
    it: Iterator[Vertex[V]] = iter(not_visited)
    neighbour: Optional[Vertex[V]] = next(it, None)
    path: List[Vertex[V]] = []
    while not path and neighbour is not None:
        visited.add(neighbour)
        path = find_path_aux(udg, neighbour, obj, visited)
        if not path:
            neighbour = next(it, None)
    return [] if not path else [org] + path

def filter_visited(all: List[Vertex[V]], visited: Set[Vertex[V]]) -> List[Vertex[V]]:
    return [v for v in all if v not in visited]

print([v.element for v in find_path_dfs(grafo, v1, v3)])

lista: List[int] = [1, 4, 5, 3, 10]
it: Iterator[int] = iter(lista)
entero: Optional[int] = next(it, None)
while entero is not None:
    print(entero % 2)
    entero = next(it, None)



