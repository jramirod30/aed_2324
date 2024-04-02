from typing import List, TypeVar, Tuple

T = TypeVar("T")


def contar_iguales(lista: List[int], a: int) -> int:  # int -> T
    if lista:  # equivale a lista != []
        if lista[0] == a:  # mejor usar el operador (result1 if cond else result2)
            return 1 + contar_iguales(lista[1:], a)  # lista[1:] es O(n)
        else:
            return contar_iguales(lista[1:], a)
    else:
        return 0


def contar_iguales1(lista: List[T], a: T, i: int = 0) -> int:
    if i < len(lista):
        return (1 if lista[i] == a else 0) + contar_iguales1(lista, a, i + 1)
    else:
        return 0


print(contar_iguales1([3, 5, 5, 2, 5, 1, 5], 5))


def buscar_elem(lista: List[T], elem: T, i: int = 0) -> int:
    if i == len(lista):
        return -1
    elif lista[i] == elem:
        return i
    else:
        return buscar_elem(lista, elem, i + 1)


print("pos:" + str(buscar_elem([3, 1, 5, 9, 11], 9)))
print("pos:" + str(buscar_elem([3, 1, 5, 9, 11], 99)))


def binary_search(lista: List[T], elem: T) -> int:
    def binary_search_aux(low: int, high: int) -> int:
        if low > high:
            return -1
        else:
            central: int = int((low + high) / 2)
            if lista[central] == elem:
                return central
            elif lista[central] < elem:
                return binary_search_aux(central + 1, high)
            else:
                return binary_search_aux(low, central - 1)

    return binary_search_aux(0, len(lista) - 1)


print(binary_search([1, 3, 5, 7, 9, 11, 13], 20))
print(binary_search([1, 3, 5, 7, 9, 11, 13], 3))


def merge_lists(lista1: List[T], lista2: List[T]) -> List[T]:
    i: int = 0
    j: int = 0
    result: List[T] = []
    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            result.append(lista1[i])
            i += 1
        else:
            result.append(lista2[j])
            j += 1
    if i < len(lista1):
        result.extend(lista1[i:])
    else:
        result.extend(lista2[j:])
    return result


def mergesort(lista: List[T]) -> List[T]:
    if len(lista) > 1:
        medio: int = int((len(lista) - 1) / 2)
        mitad1: List[T] = mergesort(lista[:medio + 1])
        mitad2: List[T] = mergesort(lista[medio + 1:])
        return merge_lists(mitad1, mitad2)
    else:
        return lista


print(f"sort: {mergesort([7, 3, 2, 16, 24, 4, 11, 9])}")


def separar_pares_impares(lista1: List[int], pares: List[int] = [],
                          impares: List[int] = [], i: int = 0) -> Tuple[List[int], List[int]]:
    if i == len(lista1):
        return pares, impares
    elif lista1[i] % 2 == 0:
        pares.append(lista1[i])
    else:
        impares.append(lista1[i])
    return separar_pares_impares(lista1, pares, impares, i + 1)


print(separar_pares_impares([5, 2, 4, 7, 1]))
