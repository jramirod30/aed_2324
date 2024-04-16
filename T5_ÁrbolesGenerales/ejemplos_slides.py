from typing import TypeVar, Optional, Iterator, List

from tads import IGeneralTree, IPosition, LinkedGeneralTree, ITree, CircularQueue

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


def sum_elems_aux(gtree: ITree[int], pos: IPosition[int]) -> int:
    """
    PRE: pos is a valid position of gtree

    POST: returns the sum of the nodes in the subtree ref
    by pos
    """
    total: int = pos.element
    # we might have more than two children
    # we need to visit all the nodes in the subtrees
    child_pos: IPosition[int]
    for child_pos in gtree.children(pos):
        total += sum_elems_aux(gtree, child_pos)
    return total


def sum_elems(gtree: ITree[int]) -> int:
    """
    PRE: gtree is not empty

    POST: returns thesum of
    the nodes in gtree
    """
    return sum_elems_aux(gtree, gtree.root)


print(sum_elems(tree))


def find_aux(gtree: ITree[T], elem: T, p: IPosition[T]) -> Optional[IPosition[T]]:
    """
    PRE: p is a valid position of gtree

    POST: returns the position of the node that contains elem
    in the subtree ref by p, if exits. Otherwise, returns None
    """
    if elem == p.element:
        return p
    else:
        # no hace falta el found de la transparencia
        it: Iterator[IPosition[T]] = gtree.children(p)
        child_pos: Optional[IPosition[T]] = next(it, None)
        pos: Optional[IPosition[T]] = None
        # As soon as elem is found in a subtree, it leaves the loop
        while pos is None and child_pos is not None:
            pos = find_aux(gtree, elem, child_pos)
            child_pos = next(it, None)
        return pos


def find(gtree: ITree[T], elem: T) -> Optional[IPosition[T]]:
    return find_aux(gtree, elem, gtree.root)


print(find(tree, 8).element)  # está
print(find(tree, 888))  # no está


def my_breadth(gtree: ITree[T]) -> List[IPosition[T]]:
    list_data: List[IPosition[T]] = []
    children: CircularQueue[IPosition[T]] = CircularQueue()
    children.add(gtree.root)
    while not children.is_empty:
        info: IPosition[T] = children.poll()
        list_data.append(info)  # visit the node
        for child in gtree.children(info):
            children.add(child)
    return list_data


for pos in my_breadth(tree):
    print(f"{pos.element}", end=', ')
