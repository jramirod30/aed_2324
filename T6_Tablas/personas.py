from typing import Dict, List, Tuple

class Person:
    def __init__(self, name: str, surname: str, identification_number: str, email: str = "", phone_number: str = ""):
        self.__name = name
        self.__surname = surname
        self.__identification_number = identification_number
        self.__email = email
        self.__phone_number = phone_number

    @property
    def name(self) -> str:
        return self.__name
        

    @property
    def surname(self) -> str:
        return self.__surname
        

    @property
    def identification_number(self) -> str:
        return self.__identification_number
        

    def __hash__(self):
        return hash((self.name, self.surname, self.identification_number))
        

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and\
        self.surname == other.surname and\
        self.identification_number == other.identification_number
        else:
            return False



personas: Dict[Person, int] = {}
person1: Person = Person("Yo", "surname yo", "990000000J", "yo@tu", "77777877")
person2: Person = Person("Ana", "Ruiz", "990000000T", "yo@tu", "77777877")
person3: Person = Person("Pepe", "Ramirez", "11111111K", "yo@tu", "77777877")

personas[person1] = 13
personas[person2] = 33
personas[person3] = 57

print(personas)
