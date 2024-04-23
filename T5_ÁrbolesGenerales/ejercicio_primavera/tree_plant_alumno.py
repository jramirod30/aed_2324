from typing import Optional, TypeVar, Iterator

from tads import IGeneralTree, LinkedGeneralTree, IPosition, ITree

from flower import Flower, TColor, TShape

T = TypeVar("T")

# elements of internal nodes are None or flowers
TreePlant = IGeneralTree[Optional[Flower]]

tree_plant: TreePlant = LinkedGeneralTree()
p1: IPosition[Optional[Flower]] = tree_plant.add_root(Flower(TColor.GREEN, TShape.OK))
p2: IPosition[Optional[Flower]] = tree_plant.add_child_first(p1, Flower(TColor.GREEN, TShape.OK))
p3: IPosition[Optional[Flower]] = tree_plant.add_child_last(p1, Flower(TColor.GREEN, TShape.OK))
tree_plant.insert_sibling_before(p3, Flower(TColor.RED, TShape.OK))
p4: IPosition[Optional[Flower]] = tree_plant.add_child_first(p2, Flower(TColor.GREEN, TShape.OK))
p6: IPosition[Optional[Flower]] = tree_plant.insert_sibling_after(p4, Flower(TColor.GREEN, TShape.OK))
tree_plant.insert_sibling_before(p6, Flower(TColor.RED, TShape.OK))
tree_plant.add_child_first(p3, Flower(TColor.GREEN, TShape.OK))
p8 = tree_plant.add_child_last(p3, Flower(TColor.BLUE, TShape.OK))
p9 = tree_plant.add_child_first(p8, Flower(TColor.GREEN, TShape.BROKEN))

print(tree_plant)


def is_spring(tree: TreePlant) -> bool:
    """
    PRE: tree is not empty

    POST: indicates if the tree plant has more than 50% of
    its flowers in spring.

    A flower is in spring if it is ok and not brown
    """
    aux = is_spring_aux(tree, tree.root)
    print(aux, tree.size())
    return tree.size() * 0.5 < aux


def is_spring_aux(tree: TreePlant, pos: IPosition[Optional[Flower]]) -> int:
    total: int = 0
    if (pos.element is not None and pos.element.color != TColor.BROWN and
            TShape.OK == pos.element.shape):
        total += 1
    it: Iterator[IPosition[Optional[Flower]]] = tree.children(pos)
    child_pos: Optional[IPosition[Optional[Flower]]] = next(it, None)
    while child_pos is not None and total/tree.size() <= 0.5:
        total += is_spring_aux(tree, child_pos)
        child_pos = next(it, None)
    return total


print(is_spring(tree_plant))
