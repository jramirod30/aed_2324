from typing import List, TypeVar

T = TypeVar("T")


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


def sumatorio(lista: List[int], k: int = 0) -> int:
    if k < len(lista):
        return lista[k] + sumatorio(lista, k + 1)
    return 0


def posiciones(lista: List[T], dato: T, i: int = 0) -> List[int]:
    if i < len(lista):
        if lista[i] == dato:
            return [i] + posiciones(lista, dato, i + 1)
        else:
            return posiciones(lista, dato, i + 1)
    else:
        return []


def posiciones1(lista: List[T], dato: T, i: int = 0) -> List[int]:
    if i < len(lista):
        return (([i] if lista[i] == dato else []) +
                posiciones1(lista, dato, i + 1))
    else:
        return []


print(posiciones1([3, 3, 12, 25, 67, 3], 3))


def filtrar(num: int, lista: List[int],
            result: List[int], i: int = 0) -> List[int]:
    if i >= len(lista):
        return result
    elif lista[i] % num == 0:
        result.append(lista[i])
        return filtrar(num, lista, result, i + 1)
    else:
        return filtrar(num, lista, result, i + 1)


def xor(lista1: List[int], lista2: List[int], i: int = 0) -> List[int]:
    if i < len(lista1):
        #  return [lista1[i]+lista2[i] % 2] + xor(lista1,lista2, i+1)
        return ([1] if lista1[i] + lista2[i] == 1 else [0]) \
            + xor(lista1, lista2, i + 1)
    else:
        return []


def max_rec(list: List[int], acc: int = list[0], i: int = 1) -> int:
    if i == len(list):
        return acc

    if list[i] > acc:
        acc = list[i]

    return max_rec(list, acc, i + 1)


def intercalar(lista1: List[int], lista2: List[int],
               k: int = 0, result: List[int] = []) -> List[int]:
    longitud1: int = len(lista1)
    longitud2: int = len(lista2)
    if k >= max(longitud1, longitud2):
        return result
    if k < min(longitud1, longitud2):
        result.append(lista1[k])
        result.append(lista2[k])
        return intercalar(lista1, lista2, k + 1, result)
    else:
        if k < longitud2:
            result.extend(lista2[k:])
        else:
            result.extend(lista1[k:])
        return result
