from typing import TypeVar

from tads import IGeneralTree, LinkedGeneralTree, IPosition, ITree

T = TypeVar("T")

tree: IGeneralTree[int] = LinkedGeneralTree()
p1: IPosition[int] = tree.add_root(1)
p2: IPosition[int] = tree.add_child_first(p1, 2)
p3: IPosition[int] = tree.add_child_last(p1, 3)

tree.insert_sibling_before(p3, 10)
p4: IPosition[int] = tree.add_child_first(p2, 4)
p6: IPosition[int] = tree.insert_sibling_after(p4, 6)
tree.insert_sibling_before(p6, 5)
tree.add_child_first(p3, 7)
tree.add_child_first(tree.add_child_last(p3, 8), 9)

print(tree)


def contar_nodos_internos_aux(gtree: ITree[T], p: IPosition[T]) -> int:
    if gtree.is_leaf(p):
        return 0
    total: int = 1
    node: IPosition[T]
    for node in gtree.children(p):
        total += contar_nodos_internos_aux(gtree, node)
    return total


def contar_nodos_internos(gtree: ITree[T]) -> int:
    return contar_nodos_internos_aux(gtree, gtree.root)


print(contar_nodos_internos(tree))


def depth(gtree: ITree[T], p: IPosition[T]) -> int:
    high: int = 0
    while p != gtree.root:
        high += 1
        p = gtree.parent(p)
    return high


print(depth(tree, p6))


def depth_rec(gtree: ITree[T], p: IPosition[T]) -> int:
    if gtree.is_root(p):
        return 0
    else:
        return 1 + depth_rec(gtree, gtree.parent(p))


print(depth(tree, p6))
