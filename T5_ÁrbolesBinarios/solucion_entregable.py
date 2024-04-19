from typing import Optional, TypeVar, List

from tads import IBinaryTree, LinkedBinaryTree, IPosition

T = TypeVar("T")

tree: IBinaryTree[int] = LinkedBinaryTree()

root: IPosition[int] = tree.add_root(1)

n2: IPosition[int] = tree.add_left(root, 2)
tree.add_left(n2, 4)
tree.add_right(n2, 5)

n3: IPosition[int] = tree.add_right(root, 3)
tree.add_left(n3, 6)
n7: IPosition[int] = tree.add_right(n3, 7)
tree.add_left(n7, 8)

tree1: IBinaryTree[int] = LinkedBinaryTree()

root: IPosition[int] = tree1.add_root(1)

n2: IPosition[int] = tree1.add_left(root, 2)
tree1.add_left(n2, 4)
tree1.add_right(n2, 5)

n3: IPosition[int] = tree1.add_right(root, 3)
tree1.add_left(n3, 6)
n7: IPosition[int] = tree1.add_right(n3, 7)


# tree1.add_left(n7, 8)

def equals_aux(btree1: IBinaryTree[T], btree2: IBinaryTree[T],
               p1: Optional[IPosition], p2: Optional[IPosition]) -> bool:
    if p1 is not None and p2 is not None:
        return (p1.element == p2.element and
                equals_aux(btree1, btree2, btree1.left(p1), btree1.left(p2)) and
                equals_aux(btree1, btree2, btree1.right(p1), btree2.right(p2)))
    else:
        return p1 is None and p2 is None


def equals(btree1: IBinaryTree[T], btree2: IBinaryTree[T]) -> bool:
    if not btree1.is_empty and not btree2.is_empty:
        return (btree1.size() == btree2.size() and
                equals_aux(btree1, btree2, btree1.root,
                           btree2.root))
    else:
        return btree1.is_empty and btree2.is_empty


print(equals(tree, tree))  # True
print(equals(tree, tree1))  # False


def find_path_aux(btree: IBinaryTree[T], elem: T, pos: Optional[IPosition[T]], path: List[IPosition[T]]) -> bool:
    if pos is None:
        return False
    path.append(pos)
    if pos.element == elem:
        return True
    if find_path_aux(btree, elem, btree.left(pos), path):
        return True
    elif find_path_aux(btree, elem, btree.right(pos), path):
        return True
    path.pop()
    return False


def find_path(btree: IBinaryTree[T], elem: T) -> List[IPosition[T]]:
    if btree.is_empty:
        return []
    path: List[IPosition[T]] = []
    if find_path_aux(btree, elem, btree.root, path):
        return path
    return []


print([a.element for a in find_path(tree, 8)])  # [1, 3, 7, 8]
print([a.element for a in find_path(tree, 88)])  # []


def find_path1(btree: IBinaryTree[T], elem: T) -> List[IPosition[T]]:
    if btree.is_empty:
        return []
    path: List[IPosition[T]] = \
        find_path_aux1(btree, elem, btree.root)
    path.reverse()
    return path


def find_path_aux1(btree: IBinaryTree[T], elem: T,
                   p: IPosition[T]) -> List[IPosition[T]]:
    if p:
        if elem == p.element:
            return [p]
        else:
            path_aux: List[IPosition[T]] = \
                find_path_aux1(btree, elem, btree.left(p))
            if not path_aux:
                path_aux = \
                    find_path_aux1(btree, elem, btree.right(p))
            if path_aux:
                path_aux.append(p)
                return path_aux
            else:
                return []


print([a.element for a in find_path1(tree, 8)])  # [1, 3, 7, 8]
print([a.element for a in find_path1(tree, 88)])  # []

def find_aux(btree: IBinaryTree[T], elem: T, p: Optional[IPosition[T]]) -> Optional[IPosition[T]]:
    if p:
        if p.element == elem:
            return p
        else:
            a: Optional[IPosition[T]] = find_aux(btree, elem, btree.left(p))
            if a is not None:
                return a
            else:
                return find_aux(btree, elem, btree.right(p))
    else:
        return None


def find(btree: IBinaryTree[T], elem: T) -> Optional[IPosition[T]]:
    return find_aux(btree, elem, btree.root)


def replace(btree: IBinaryTree[T], old: T, new: T) -> None:
    if not btree.is_empty:
        a: Optional[IPosition[T]] = find(btree, old)
        if a is not None:
            btree.set(a, new)


replace(tree, 5, 55)
replace(tree, 44, 444)  # sin efecto
print(tree)