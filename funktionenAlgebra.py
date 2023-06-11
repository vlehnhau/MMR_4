import matplotlib.pyplot as plt
import numpy as np
import math

# Aufgabe 2

class Function:
    def __init__(self, fun):
        self.fun = fun

    def __call__(self, x):
        return self.fun(x)

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




f = Function(lambda x: x*2)
g = Function(lambda x: x+1)

#Test Add
Addfg = AddFunction(f, g)
#print(f(3) + g(2))              #3*2 + 2+1 = 9
#print(Addfg(1))                 #1*2 + 1+1 = 4

#Test Sub
Subfg = SubFunction(f, g)
#print(f(3) - g(2))              #3*2 - 2+1 = 3
#print(Subfg(1))                 #1*2 - 1+1 = 0

#Test Mul
Mulfg = MulFunction(f, g)
#print(f(3) * g(2))              #3*2 * 2+1 = 18
#print(Mulfg(1))                 #1*2 * 1+1 = 4

#Test Div
Divfg = DivFunction(f, g)
#print(f(3) / g(2))              #3*2 / 2+1 = 2
#print(Divfg(1))                 #1*2 / 1+1 = 1

#Test Pow
Powfg = PowFunction(f, g)
#print(f(3) ** g(2))             #3*2 ** 2+1 = 216
#print(Powfg(1))                 #1*2 ** 1+1 = 4

#Test Matmul
Matmulfg = MatmulFunction(f, g)
#print(Matmulfg(3))                 #(3+1)*2 = 8



id = Function(lambda x: x)
con = lambda c: Function(lambda x: c)
sin = Function(lambda x: math.sin(x))
cos = Function(lambda x: math.cos(x))
exp = Function(lambda x: math.exp(x))
ln = Function(lambda x: math.log(x))


f = sin / cos + exp
#print(f(42), " == ", math.sin(42) / math.cos(42) + math.exp(42))

def beispielFunktion():
    f = Function(lambda x: np.sin(cos(x) + x ** 2))
    x = np.linspace(-5, 5, 1000)
    y = [f(val) for val in x]
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('f(x) = sin(cos(x) + x^2)')
    plt.show()

if __name__ == '__main__':
    beispielFunktion()