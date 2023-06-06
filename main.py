import matplotlib.pyplot as plt
import numpy as np
from math import *


# Aufgabe 4.1.1

# toDo: Theoriefragen

# a)

# Hier 2x^3 + 3x^2 - 4x + 1
# coe = [2, 3, -4, 1]
# coeAbl = [6, 6, -4]

# print(np.poly1d(coe))

# start = -10
# stop = 10
# num = 100

# x_values = np.linspace(start, stop, num)
# y_values = np.polyval(coe, x_values)
# y_valuesAbl = np.polyval(coeAbl, x_values)

# step_size = (stop - start) / (num - 1)

# Ausgabe der berechneten Werte
# print("Function")
# for x, y in zip(x_values, y_values):
#    print(f"Für x = {x:.2f} ist y = {y:.2f}")


# numerische Ableitung

# def num_Abl(y_val, h):
#    return (y_val[2:] - y_val[:-2]) / (2 * h)


# nAbl = num_Abl(y_values, step_size)

# print("Ableitung")
# for x, y in zip(nAbl, y_values):
#    print(f"Für x = {x:.2f} ist y = {y:.2f}")

# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.plot(x_values, y_values)
# ax.plot(x_values[1:-1], nAbl)
# ax.plot(x_values, y_valuesAbl)
# plt.show()


# numerische Ableitung Extrema

# def find_ex(y_val, h):
#    abl = num_Abl(y_val, h)


# Versuch 2


# Aufgabe 1:

def get_points_of_function(fun, step_size, start, end):
    return_val = [[], []]
    while start <= end:
        return_val[0].append(start)
        return_val[1].append(fun(start))
        start += step_size

    return return_val


def get_num_Abl(point_list):
    return_val = [[], []]
    step_size = point_list[0][1] - point_list[0][0]
    y_val = np.array(point_list[1])
    return_val[0] = point_list[0][1:-1]
    return_val[1] = (y_val[2:] - y_val[:-2]) / (2 * step_size)

    return return_val

def get_ex_num_Abl(point_list):
    pass


if __name__ == '__main__':
    zero_pointer = [1, 2, 3]
    function = np.poly1d(zero_pointer, True)

    points_of_fun = get_points_of_function(function, 1, -10, 10)
    points_of_num_Abl = get_num_Abl(points_of_fun)
    points_of_ex_num_Abl = get_ex_num_Abl

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(points_of_num_Abl[0], points_of_num_Abl[1])
    plt.show()
