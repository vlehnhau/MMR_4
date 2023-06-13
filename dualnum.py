from funktionenAlgebra import *
from main import *


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
        # (f/g)' = (f'g - fg') / g^2
        return DualNumber(self.wert / other.wert,
                          (self.ableitung * other.wert - self.wert * other.ableitung) / (other.wert ** 2))

    def __pow__(self, power, modulo=None):
        # (f^n)' = n * f^(n-1) * f'.
        return DualNumber(self.wert ** power, power * self.wert ** (power - 1) * self.ableitung)


class DualFunction(Function):
    pass


class Sin(DualFunction):
    def __call__(self, x):
        return DualNumber(sin(x.wert), cos(x.wert) * x.ableitung)


class Cos(DualFunction):
    def __call__(self, x):
        return DualNumber(cos(x.wert), -sin(x.wert) * x.ableitung)


class Tan(DualFunction):
    def __call__(self, x: DualNumber):
        cos_val = cos(x.wert)
        return DualNumber(math.tan(x.wert), x.ableitung / (cos_val ** 2))


class Exp(DualFunction):
    def __call__(self, x):
        return DualNumber(exp(x.wert), exp(x.wert) * x.ableitung)


class Ln(DualFunction):
    def __call__(self, x):
        return DualNumber(log(x.wert), (1 / x.wert) * x.ableitung)


class SinOne(DualFunction):
    def __call__(self, x: DualNumber):
        return DualNumber(math.sin(1 / x.wert), -math.cos(1 / x.wert) / (x.wert * x.wert))


if __name__ == '__main__':
    faketan = Tan()
    fakesin = Sin()
    fakecos = Cos()
    faketan_two = fakesin / fakecos
    fakesinone = SinOne()

    tanpoints = []
    tanfakepoints = []
    sinonefakepoints = []

    val_x = []

    i = -500

    while i < 500:
        x = DualNumber(i, 1)

        tan_val = faketan(x)
        faketan_val = faketan_two(x)
        sinone_val = fakesinone(x)

        sinonefakepoints.append(sinone_val.wert)
        tanpoints.append(tan_val.wert)
        tanfakepoints.append(faketan_val.wert)
        # print("(", tan(i), ", ", tan_val.wert, ", ", faketan_val.wert, ")")

        val_x.append(i)


        i += 0.001

    fig, ax1 = plt.subplots()
    plt.autoscale(False)
    plt.xlim([-10, 10])
    plt.ylim([-10, 10])
    ax1.plot(val_x, tanpoints, "r")
    ax1.plot(val_x, tanfakepoints, "b")
    plt.show()

    points_of_fun = get_points_of_function(sin1, 0.001, -10, 10)

    fig, ax2 = plt.subplots()
    plt.autoscale(False)
    plt.xlim([-10, 10])
    plt.ylim([-2.5, 2.5])
    ax2.plot(points_of_fun[0], points_of_fun[1], "b")
    ax2.plot(val_x, sinonefakepoints, "r")
    plt.show()
