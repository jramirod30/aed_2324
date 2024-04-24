from typing import List, Dict, Tuple

censo: List[Tuple[str, str]] = [
    ("Toledo", "Juan"),
    ("Madrid", "Pepe"),
    ("Toledo", "Luis"),
    ("Bilbao", "Ana"),
    ("Jaen", "Eva"),
]


def get_max_poblacion(censo: List[Tuple[str, str]]) -> str:
    """
    PRE: censo is not empty
    POST: return the city with
        the largest population
    """
    contador: Dict[str, int] = get_population_table(censo)
    # Hemos creado el diccionario
    max_population: int = 0
    max_city: str = ""
    for city in contador:
        if contador[city] > max_population:
            max_population = contador[city]
            max_city = city
    return max_city


def get_population_table(censo: List[Tuple[str, str]]) -> Dict[str, int]:
    """
    PRE: censo is not empty
    POST: return a dictionary with the
    population of each city
    """
    contador: Dict[str, int] = {}
    for par in censo:
        if par[0] in contador:
            contador[par[0]] += 1
        else:
            contador[par[0]] = 1
    return contador



print(get_max_poblacion(censo))
print(get_population_table(censo))
