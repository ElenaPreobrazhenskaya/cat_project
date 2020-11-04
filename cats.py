# coding=utf-8
import math
from re import S


class Cat:
    def __init__(self):
        pass

    def answer_me(self, string):
        return string

class Triangular(Cat):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_triangle_description(self):
        if (self.a == self.b == self.c):
            return "Это равносторонний треугольный кот"
        return "Это треугольный кот"

class Circle(Cat):
    def __init__(self, r):
        self.r = r
        super().__init__()

    def get_circle_description(self):
        S = math.pi * self.r**2
        return f"Это круглый кот, его площадь {S}"

class Square(Cat):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_square_description(self):
        if self.a == self.b:
            return "Это квадратный кот"
        return "Это прямоугольный кот"

def recogise_cat(cat:Cat) -> str:
    if isinstance(cat, Triangular):
        return cat.get_triangle_description()
    if isinstance(cat, Circle):
        return cat.get_circle_description()
    if isinstance(cat, Square):
        return cat.get_square_description()
    else:
        return "Это не кот"


def main():
    cat_1 = Triangular(2,2,2)
    cat_2 = Circle(3)
    cat_3 = Square(2,2)

    print(recogise_cat(cat_1))
    print(recogise_cat(cat_2))
    print(recogise_cat(cat_3))

main()