from __future__ import annotations
from typing import List, Set, TypeVar, Tuple
T = TypeVar("T")
V = TypeVar("V")

# Dada una lista l1, devolver un conjunto con los mismos elementos
def elems(l1: List[T]) -> Set[T]:
    conjunto: Set[T] = set()
    for i in l1:
        conjunto.add(i)
    return conjunto
# Hallar la intersección de l1 y l2
def elems_comunes(l1, l2: List[T]) -> Set[T]:
    conjunto1: Set[T] = elems(l1)
    conjunto2: Set[T] = elems(l2)
    return conjunto1 & conjunto2
# Devolver true si l2 es un subconjunto de l1
def esta_incluida(l1, l2: List[T]) -> bool:
    conjunto1: Set[T] = elems(l1)
    conjunto2: Set[T] = elems(l2)
    return conjunto2 <= conjunto1

# Eliminar de l1 todos los elementos que están en l2
def extraer_elems(l1, l2: List[T]) -> Set[T]:
    conjunto1: Set[T] = elems(l1)
    conjunto2: Set[T] = elems(l2)
    return conjunto1 - conjunto2

# Devolver el producto cartesiano de dos conjuntos s1, s2
def producto_cartesiano(s1: Set[T], s2: Set[V]) -> Set[(T, V)]:
    result : Set[(T, V)]
    for x in s1:
        for y in s2:
            result.add((x, y))
    return result
    # ALTERNATIVA:
    # return {(x,y) for x in s1 for y in s2}

# Devolver los elementos que están en s1 o en s2, pero no en ambos
def elems_no_comunes(s1: Set[T], s2: Set[T]) -> Set[T]:
    return (s1 | s2) - (s1 & s2)

# Dada una lista de números, encontrar todos los pares (a, b) que sumen
# a + b = objetivo, utilizando conjuntos
def encuentra_pares_suma(nums: List[int], objetivo: int) -> List[Tuple[int, int]]:
    nums_set: Set[int] = elems(nums)
    respuesta: List[Tuple[int, int]] = []
    for x in nums:
        if objetivo - x in nums_set and (objetivo - x <= objetivo/2):
            respuesta.append((x, objetivo - x))
    return respuesta

l1: List[int] = [0, 1, 2, 3, 4, 6]
print(encuentra_pares_suma(l1, 6))
