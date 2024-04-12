from typing import Optional, TypeVar

from tads import IBinaryTree, LinkedBinaryTree, IPosition

T = TypeVar("T")

tree: IBinaryTree[int] = LinkedBinaryTree()

root: IPosition[int] = tree.add_root(1)

n2: IPosition[int] = tree.add_left(root, 2)
tree.add_left(n2, 4)
tree.add_right(n2, 11)

n3: IPosition[int] = tree.add_right(root, 3)
tree.add_left(n3, 12)
n7: IPosition[int] = tree.add_right(n3, 7)
tree.add_left(n7, 8)

print(tree)


def contar_hojas_aux(btree: IBinaryTree[T],
                     p: Optional[IPosition[T]]) -> int:
    if p:
        if btree.is_leaf(p):
            return 1
        else:
            return (contar_hojas_aux(btree, btree.left(p)) +
                    contar_hojas_aux(btree, btree.right(p)))
    else:
        return 0


def contar_hojas(btree: IBinaryTree[T]) -> int:
    return contar_hojas_aux(btree, btree.root)


def contar_ocurrencias_aux(btree: IBinaryTree[T], elem: T,
                           p: Optional[IPosition[T]]) -> int:
    if p:
        if p.element == elem:
            return (1 + contar_ocurrencias_aux(btree, elem, btree.left(p)) +
                    contar_ocurrencias_aux(btree, elem, btree.right(p)))
        else:
            return contar_ocurrencias_aux(btree, elem, btree.left(p)) + \
                contar_ocurrencias_aux(btree, elem, btree.right(p))
    else:
        return 0


def contar_ocurrencias(btree: IBinaryTree[T], elem: T) -> int:
    return contar_ocurrencias_aux(btree, elem, btree.root)


print(contar_ocurrencias(tree, 111))


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


print(find(tree, 7777))