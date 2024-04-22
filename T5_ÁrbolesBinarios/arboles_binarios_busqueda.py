from typing import TypeVar, Optional

from tads.position.iposition import IPosition
from tads.tree.linked_binary_tree import IBinaryTree
from tads.tree.linked_binary_tree import LinkedBinaryTree

T = TypeVar('T')

tree: LinkedBinaryTree[int] = LinkedBinaryTree()
tree.add_root(10)
nl: IPosition = tree.add_left(tree.root, 2)
nl1 = tree.add_left(nl, 1)
tree.add_right(nl, 5)

nr: IPosition = tree.add_right(tree.root, 30)
tree.add_left(nr, 20)
nr1 = tree.add_right(nr, 70)
nr2 = tree.add_right(nr1, 80)

print("tam " + str(tree.size()))

print(tree)


def find_position(tree: IBinaryTree[T], search: T) -> Optional[IPosition[T]]:
    """
    **PRE:** tree is a not empty binary search tree

    **POST:** If data is in the tree returns its position otherwise return None
    """
    def find_position_aux(tree2: IBinaryTree[T], searching: T,
                          pos: IPosition[str]) -> Optional[IPosition[str]]:
        if pos is None or pos.element == searching:
            return pos
        elif searching < pos.element:
            return find_position_aux(tree2, searching, tree2.left(pos))
        else:
            return find_position_aux(tree2, searching, tree2.right(pos))

    return find_position_aux(tree, search, tree.root)


print(find_position(tree, 20).element)  # found
print(find_position(tree, 200))  # not found


def add_aux(btree: IBinaryTree[T], e: T, p: IPosition[T]) -> None:
    """
    PRE: btree is a binary search tree and p is valid position in btree

    POST: add e to subtree ref by p so that the new subtree is still a binary search tree
    """
    if e < p.element:
        if btree.left(p) is None:
            btree.add_left(p, e)
        else:
            add_aux(btree, e, btree.left(p))
    else:
        if btree.right(p) is None:
            btree.add_right(p, e)
        else:
            add_aux(btree, e, btree.right(p))


def add(btree: IBinaryTree[T], e: T) -> None:
    """
    PRE: btree is a binary search tree

    POST: add e to btree so that the new btree is still a binary search tree
    """
    if btree.is_empty:
        btree.add_root(e)
    else:
        add_aux(btree, e, btree.root)


add(tree, 25)
add(tree, 19)

print(tree)


def find_max(btree: IBinaryTree, pos_max: IPosition[T]) -> IPosition[T]:
    """
    PRE: btree is not empty BST and pos_max is a valid position in btree

    POST: returns the position of the max in the subtree ref by pos_max
    """
    pos_aux: IPosition[T] = pos_max
    while btree.right(pos_aux):
        pos_aux = btree.right(pos_aux)
    return pos_aux


def move_up_node(btree: IBinaryTree[T], target: IPosition[T], source: IPosition[T]):
    """
    PRE: btree is not empty, and target and source are valid
    positions in btree

    POST: elem of source is copied to target and subtree ref by
    source is removed
    """
    btree.set(target, source.element)
    btree.remove_subtree(source)


def delete_aux(btree: IBinaryTree[T], e: T, pos: IPosition[T]) -> None:
    """
    PRE: btree is a BST and e is in subtree ref by pos
    and pos is a valid position in btree

    POST: e is removed from the subtree ref by pos and btree is still a BST
    """
    if e < pos.element:
        delete_aux(btree, e, btree.left(pos))
    elif e > pos.element:
        delete_aux(btree, e, btree.right(pos))
    else:  # delete the node
        if btree.left(pos) and btree.right(pos):  # case 3
            pos_max: IPosition[T] = find_max(btree, btree.left(pos))
            btree.set(pos, pos_max.element)
            if btree.left(pos_max):
                move_up_node(btree, pos_max, btree.left(pos_max))
            else:
                btree.remove_subtree(pos_max)
        else:
            if btree.left(pos):  # case 2
                move_up_node(btree, pos, btree.left(pos))
            elif btree.right(pos):  # case 2
                move_up_node(btree, pos, btree.right(pos))
            else:  # case 1
                btree.remove_subtree(pos)


def delete(btree: IBinaryTree[T], e: T) -> None:
    """
    PRE: btree is a BST and e is in btree

    POST: e is removed from btree and btree is still a BST
    """
    if not btree.is_empty:
        delete_aux(btree, e, btree.root)


add(tree, 4)
print(tree)
delete(tree, 5)
print(tree)
