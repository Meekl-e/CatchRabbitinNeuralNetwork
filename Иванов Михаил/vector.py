from math import hypot, pi
from numpy import arccos, arctan, copysign


class Vector2:
    x = 0
    y = 0
    strPrec = '{:.' + str(6) + 'f}'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.strPrec.format(self.x)}; {self.strPrec.format(self.y)})'

    def __repr__(self):
        return self.__str__()

    def __reversed__(self):
        return Vector2(self.y, self.x)

    def __neg__(self):
        return Vector2(-self.x, -self.y)

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int):
        return Vector2(self.x * other, self.y * other)

    def __truediv__(self, other: int):
        return Vector2(self.x / other, self.y / other)

    def __mod__(self, other):  # скалярное произведение
        return self.x * other.x + self.y * other.y

    def __xor__(self, other):  # угол
        return arccos((self % other) / (abs(self) * abs(other)))

    def __abs__(self):  # длина
        return hypot(abs(self.x), abs(self.y))


class Point:
    pos = Vector2(0, 0)

    def __init__(self, pos):
        self.pos = Vector2(*pos)

    def __str__(self):
        return f'Точка: {self.pos}'

    def __repr__(self):
        return f'Точка: {self.pos}'


def azimuth(center, poi):
    return (90 - arctan((poi.y - center.y) / (poi.x - center.x)) * 180 / pi + -90 * (copysign(-1, (poi.x - center.x)) + 1)) % 360


class Line:
    a = 0
    b = 0
    c = 0

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'{self.a}x + {self.b}x + {self.c} = 0'

    def __repr__(self):
        return self.__str__()