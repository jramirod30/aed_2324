from tads import IBinaryTree, LinkedBinaryTree, IPosition

from typing import TypeVar

T = TypeVar("T")

expresion: IBinaryTree[str] = LinkedBinaryTree()
n: IPosition[str] = expresion.add_root("+")
n1: IPosition[str] = expresion.add_left(n, "*")

n2: IPosition[str] = expresion.add_right(n, "/")
expresion.add_left(n1, "4")
expresion.add_right(n1, "6")
expresion.add_left(n2, "8")
n3: IPosition[str] = expresion.add_right(n2, "-")
#  expresion.add_left(n3, "9")
expresion.add_right(n3, "5")

print(expresion)

print(eval("((4*6)+(8/(9-5)))"))


expresion1: IBinaryTree[str] = LinkedBinaryTree()
n_plus: IPosition[str] = expresion1.add_root("+")
n5: IPosition[str] = expresion1.add_left(n_plus, "5")

n_minus: IPosition[str] = expresion1.add_right(n_plus, "-")
expresion1.add_right(n_minus, "6")

print(expresion1)


def eval_aux(exp: IBinaryTree[str], p: IPosition[str]) -> str:
    result: str = ""
    if exp.left(p):
        result += f"({eval_aux(exp, exp.left(p))})"
    result += f"{p.element}"
    if exp.right(p):
        result += f"({eval_aux(exp, exp.right(p))})"
    return result


print(eval(eval_aux(expresion, expresion.root)))
