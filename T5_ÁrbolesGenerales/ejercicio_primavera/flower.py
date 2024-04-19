from enum import Enum


class TColor(Enum):
    GREEN = 0
    YELLOW = 1
    BROWN = 2
    RED = 3
    BLUE = 4


class TShape(Enum):
    OK = 0
    BROKEN = 1


class Flower:
    def __init__(self, color: TColor = TColor.GREEN, shape: TShape = TShape.OK):
        self.__color = color
        self.__shape = shape

    @property
    def color(self) -> TColor:
        return self.__color

    @property
    def shape(self) -> TShape:
        return self.__shape

    def __str__(self) -> str:
        return str(self.__shape) + " " + str(self.__color)
