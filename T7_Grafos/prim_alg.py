import sys
from typing import TypeVar, Set, Dict, Optional

from tads import Edge
from tads.graph import UndirectedAdjacencyListGraph
from tads.graph.elements import Vertex
from tads.graph.iundirected_graph import IUndirectedGraph
from tads.position import IPosition
from tads.tree.igeneral_tree import IGeneralTree
from tads.tree.linked_general_tree import LinkedGeneralTree

V = TypeVar('V')
E = TypeVar('E')

g: IUndirectedGraph[int, int] = UndirectedAdjacencyListGraph()
v6 = g.insert_vertex(6)
v1 = g.insert_vertex(1)
v2 = g.insert_vertex(2)
v3 = g.insert_vertex(3)
v4 = g.insert_vertex(4)
v5 = g.insert_vertex(5)

e1 = g.insert_edge(v1, v2, 7)
g.insert_edge(v1, v3, 9)
g.insert_edge(v1, v6, 14)
g.insert_edge(v2, v3, 10)
g.insert_edge(v2, v4, 15)
g.insert_edge(v3, v4, 11)
g.insert_edge(v3, v6, 2)
g.insert_edge(v4, v5, 6)
g.insert_edge(v5, v6, 9)

print(g)

total: int = 0


def get_closest_to_tree(
        distances: Dict[Vertex[V], int], vertices_out_tree: Set[Vertex[V]]
) -> Vertex[V]:
    global total  # to obtain the sum of edges in the spanning tree
    min_node: Optional[Vertex[V]] = None
    min_dist: int = sys.maxsize
    for v in vertices_out_tree:
        if distances[v] < min_dist:
            min_dist = distances[v]
            min_node = v
    total += min_dist
    return min_node


def update_distances_to_tree(udg: IUndirectedGraph[V, E],
                             vertices_out_tree: Set[Vertex[V]],
                             new_node_in_tree: Vertex[V],
                             distances: Dict[Vertex[V], int],
                             closest_tree_nodes: Dict[Vertex[V], Vertex[V]]) -> None:
    node: Vertex[V]
    edge: Edge[V, E]
    for edge in udg.edges_of(new_node_in_tree):
        node = edge.opposite(new_node_in_tree)
        if node in vertices_out_tree:
            if edge.element < distances[node]:
                distances[node] = edge.element
                closest_tree_nodes[node] = new_node_in_tree


def prim_algorithm(udg: IUndirectedGraph[V, E]) -> IGeneralTree[V]:
    """
    PRE: udg is connected and weighted

    POST: return the minimum spanning tree of udg
    """
    vertices_out_tree: Set[Vertex[V]] = set(udg.vertices())
    tree: IGeneralTree[V] = LinkedGeneralTree()
    # mapping between graph nodes and tree nodes
    map_nodes_pos: Dict[Vertex[V], IPosition[V]] = {}
    # keep the min distances from the tree to the nodes out of the tree
    distances: Dict[Vertex[V], int] = {}
    # keep the node of the tree closest to each node out of the tree
    closest_tree_nodes: Dict[Vertex[V], Vertex[V]] = {}
    for v in udg.vertices():
        distances[v] = sys.maxsize - 1

    # take an arbitrary node from the graph
    closest_node_to_tree = get_closest_to_tree(distances, vertices_out_tree)
    map_nodes_pos[closest_node_to_tree] = tree.add_root(closest_node_to_tree.element)
    vertices_out_tree.remove(closest_node_to_tree)
    update_distances_to_tree(udg, vertices_out_tree, closest_node_to_tree, distances, closest_tree_nodes)

    while len(vertices_out_tree) > 0:
        # select the closest node out the tree to the tree
        closest_node_to_tree = get_closest_to_tree(distances, vertices_out_tree)
        # add this node to the tree and define the mapping between the tree pos and this node
        map_nodes_pos[closest_node_to_tree] = \
            tree.add_child_last(map_nodes_pos[closest_tree_nodes[closest_node_to_tree]],
                                closest_node_to_tree.element)
        vertices_out_tree.remove(closest_node_to_tree)
        # As a result of having a new node in the tree, the min dist to the nodes out of the tree could change
        # So, distances and closest_tree_nodes are reviewed and updated, if needed
        update_distances_to_tree(udg, vertices_out_tree, closest_node_to_tree, distances, closest_tree_nodes)

    return tree


print(prim_algorithm(g))

print(total - sys.maxsize + 1)
