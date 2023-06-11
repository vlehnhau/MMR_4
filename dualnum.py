from math import *
from funktionenAlgebra import *


class DualNumber:
    def __init__(self, wert, ableitung):
        self.wert = wert
        self.ableitung = ableitung

    def __add__(self, other):
        return DualNumber(self.wert + other.wert, self.ableitung + other.ableitung)

    def __sub__(self, other):
        return DualNumber(self.wert - other.wert, self.ableitung - other.ableitung)

    def __mul__(self, other):
        # (fg)' = f'g + fg'
        return DualNumber(self.wert * other.wert, self.ableitung * other.wert + self.wert * other.ableitung)

    def __truediv__(self, other):
        return DualNumber(self.wert / other.wert, self.ableitung / other.wert + self.wert / other.ableitung)

    def __pow__(self, power, modulo=None):
        # (f^n)' = n * f^(n-1) * f'.
        return DualNumber(self.wert ** power, power * self.wert ** (power - 1) * self.ableitung)


class DualFunction(Function):
    def __call__(self, x: DualNumber):
        pass


class Sin(DualFunction):
    def __call__(self, x):
        return DualNumber(sin(x.wert), cos(x.wert) * x.ableitung)


class Cos(DualFunction):
    def __call__(self, x):
        return DualNumber(cos(x.wert), -sin(x.wert) * x.ableitung)


class Tan(DualFunction):
    def __call__(self, x):
        return DualNumber(tan(x.wert), (1 / (cos(x.wert)) ** 2) * x.ableitung)


class Exp(DualFunction):
    def __call__(self, x):
        return DualNumber(exp(x.wert), exp(x.wert) * x.ableitung)


class Ln(DualFunction):
    def __call__(self, x):
        return DualNumber(ln(x.wert), (1 / x.wert) * x.ableitung)


if __name__ == '__main__':
    for i in range(500):
        x = DualNumber(i, 1)
        tan_val = Tan(x)
        print("(", tan(i), ", ", tan_val.wert, ", ")
