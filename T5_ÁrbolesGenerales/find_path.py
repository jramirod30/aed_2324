from typing import TypeVar, Iterator, Optional, List

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


def find_path1(btree: ITree[T], elem: T) -> List[IPosition[T]]:
    if btree.is_empty:
        return []
    path: List[IPosition[T]] = \
        find_path_aux1(btree, elem, btree.root)
    path.reverse()
    return path


def find_path_aux1(gtree: ITree[T], elem: T,
                   p: IPosition[T]) -> List[IPosition[T]]:
    if elem == p.element:
        return [p]
    else:
        it: Iterator[IPosition[T]] = gtree.children(p)
        path_aux: List[IPosition[T]] = []
        child_pos: Optional[IPosition[T]] = next(it, None)
        while not path_aux and child_pos is not None:
            path_aux = find_path_aux1(gtree, elem, child_pos)
            child_pos = next(it, None)

        if path_aux:
            path_aux.append(p)
            return path_aux
        else:
            return []


i: IPosition[T]
for i in find_path1(tree, 9999):  # no hay camino
    print(i.element, end=", ")

#  [1, 3, 8, 9]
print([a.element for a in find_path1(tree, 9)])
