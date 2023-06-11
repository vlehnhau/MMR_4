import matplotlib.pyplot as plt
import numpy as np
import math

# Aufgabe 2

class Function:
    def __call__(self, x):
        pass

    def __add__(self, other):
        return AddFunction(self, other)
    def __sub__(self, other):
        return SubFunction(self, other)
    def __mul__(self, other):
        return MulFunction(self, other)
    def __truediv__(self, other):
        return DivFunction(self, other)
    def __pow__(self, other):
        return PowFunction(self, other)
    def __matmul__(self, other):
        return MatmulFunction(self, other)



class AddFunction(Function):
    def __init__(self, f, g):
        self.f = f
        self.g = g
    def __call__(self, x):
        return self.f(x) + self.g(x)

class SubFunction(Function):
    def __init__(self, f, g):
        self.f = f
        self.g = g
    def __call__(self, x):
        return self.f(x) - self.g(x)

class MulFunction(Function):
    def __init__(self, f, g):
        self.f = f
        self.g = g
    def __call__(self, x):
        return self.f(x) * self.g(x)

class DivFunction(Function):
    def __init__(self, f, g):
        self.f = f
        self.g = g
    def __call__(self, x):
        return self.f(x) / self.g(x)

class PowFunction(Function):
    def __init__(self, f, g):
        self.f = f
        self.g = g
    def __call__(self, x):
        return self.f(x) ** self.g(x)

class MatmulFunction(Function):
    def __init__(self, f, g):
        self.f = f
        self.g = g
    def __call__(self, x):
        return self.f(self.g(x))



class Identity(Function):
    def __call__(self, x):
        return x

class Sin(Function):
    def __call__(self, x):
        return math.sin(x)

class Cos(Function):
    def __call__(self, x):
        return math.cos(x)

class Tan(Function):
    def __call__(self, x):
        return math.tan(x)

class ArcSin(Function):
    def __call__(self, x):
        return math.asin(x)

class ArcCos(Function):
    def __call__(self, x):
        return math.acos(x)

class ArcTan(Function):
    def __call__(self, x):
        return math.atan(x)

class Exp(Function):
    def __call__(self, x):
        return math.exp(x)     #e^x

class Constant(Function):
    def __init__(self, constant):
        self.constant = constant

    def __call__(self, x):
        return self.constant

class Ln(Function):
    def __call__(self, x):
        return math.log(x)


#klassische Funktionen als Funktionsobjekte
idfun = Identity()
const = lambda c: Constant(c)
sin = Sin()
cos = Cos()
exp = Exp()
ln = Ln()

def test():
    f = sin / cos + exp
    print(f(42), " == ", math.sin(42) / math.cos(42) + math.exp(42))

    def beispielFunktion():
        f = sin @ (idfun * idfun)
        x = np.linspace(-5, 5, 1000)
        y = [f(p) for p in x]
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('f(x) = sin(cos(x) + x^2)')
        plt.show()

    beispielFunktion()

if __name__ == '__main__':
    test()