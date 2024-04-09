from typing import Optional, TypeVar

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

print(tree)


def sum_elems(btree: IBinaryTree[int], p: Optional[IPosition[int]]) -> int:
    """
    PRE: btree is not empty

    POST: return the sum of the elems in btree
    """
    if p:  # p is not None
        return p.element + sum_elems(btree, btree.left(p)) + \
            sum_elems(btree, btree.right(p))
    else:
        return 0


print(sum_elems(tree, tree.root))


def height(btree: IBinaryTree[T], p: Optional[IPosition[T]]) -> int:
    """
    PRE: btree is not empty

    POST: return the height of btree
    """
    if p is None or btree.is_leaf(p):
        return 0
    else:
        return (1 +
                max(height(btree, btree.left(p)), height(btree, btree.right(p))))


print(height(tree, tree.root))


def existe(btree: IBinaryTree[T], p: Optional[IPosition[T]], elem: T) -> bool:
    """
    PRE: btree is not empty

    POST: indicate whether elem is in btree
    """
    if p:
        return p.element == elem or existe(btree, btree.left(p), elem) \
            or existe(btree, btree.right(p), elem)
    else:
        return False


print(existe(tree, tree.root, 4))
