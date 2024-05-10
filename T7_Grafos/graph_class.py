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

print(a12.endpoints())







