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


def check_repeated_elems_aux(tree: ITree[T], p: IPosition[T], list_elems: List[T]) -> bool:
        if p.element in list_elems:
            return True
        else:
            list_elems.append(p.element)
            it: Iterator[IPosition[T]] = tree.children(p)
            child: Optional[IPosition[T]] = next(it, None)
            repeated: bool = False
            while child is not None and not repeated:
                repeated = check_repeated_elems_aux(tree, child, list_elems)
                child = next(it, None)
        return repeated


def check_repeated_elems(tree: ITree[T]) -> bool:
    return check_repeated_elems_aux(tree, tree.root, [])
