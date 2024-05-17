from typing import TypeVar, List, Dict

from tads import IDirectedGraph
from tads.graph import DirectedAdjacencyListGraph
from tads.graph.elements import Vertex
from tads.queue.circular_queue import CircularQueue
from tads.queue.iqueue import IQueue

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


def get_neighbors(g: IDirectedGraph[V, E], vertex: Vertex[V]) -> List[Vertex[V]]:
    neighbors: List[Vertex[V]] = []
    for edge in g.outgoing_edges(vertex):
        neighbors += [g.end_vertex(edge)]
    return neighbors


for v in get_neighbors(g, v1):
    print(v)


def filter_visited(candidates: List[Vertex[V]], visited_vertices: Dict[Vertex[V], Vertex[V]]) -> List[Vertex[V]]:
    result: List[Vertex[V]] = []
    for edge in candidates:
        if edge not in visited_vertices:
            result += [edge]
    return result


def build_path(org, target: Vertex[V], visited_vertices: Dict[Vertex[V], Vertex[V]]) -> List[Vertex[V]]:
    if org == target:
        return [org]
    else:
        path: List[Vertex[V]] = build_path(org, visited_vertices[target],
                                           visited_vertices)
        path.append(target)
        return path


def find_path_bfs(udg: IDirectedGraph[V, E], target: Vertex[V], org: Vertex[V]) -> List[Vertex[V]]:
    pending_nodes: IQueue[Vertex[V]] = CircularQueue()
    pending_nodes.add(org)
    visited_vertices: Dict[Vertex[V], Vertex[V]] = {org: org}
    found: bool = False
    while not found and not pending_nodes.is_empty:
        info: Vertex[V] = pending_nodes.poll()
        neighbors: List[Vertex[V]] = filter_visited(get_neighbors(udg, info),

                                                    visited_vertices)
        i: int = 0
        while i < len(neighbors) and neighbors[i] != target:
            pending_nodes.add(neighbors[i])
            visited_vertices[neighbors[i]] = info
            i += 1
        found = (i < len(neighbors))

    if found:
        path_to_target: List[Vertex[V]] = build_path(org, info, visited_vertices)
        path_to_target.append(target)
        return path_to_target
    else:
        return []


print([v.element for v in find_path_bfs(g, v5, v1)])
