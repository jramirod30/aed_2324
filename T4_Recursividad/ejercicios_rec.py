from typing import List


def multiplicar10(lista: List[int]) -> List[int]:
    if lista:
        return [lista[0] * 10] + multiplicar10(lista[1:])
    else:
        return []

#  versión que no crea sublista en la llamada rec.
def multiplicar10_1(lista: List[int], i: int = 0) -> List[int]:
    if i < len(lista):
        return [lista[i] * 10] + multiplicar10_1(lista, i + 1)
    else:
        return []


#  versión con parámetro acumulativo
def multiplicar10_2(lista: List[int], result: List[int] = [],
                    i: int = 0) -> List[int]:
    if i < len(lista):
        result.append(lista[i] * 10)
        return multiplicar10_2(lista, result, i + 1)
    else:
        return result
