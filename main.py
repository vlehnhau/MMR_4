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
    prev_point = point_list[1][0]

    for i in range(1, len(point_list[0])):
        if prev_point >= 0 and point_list[1][i] < 0:
            print("found max")
        if prev_point < 0 and point_list[1][i] >= 0:
            print("found min")

        prev_point = point_list[1][i]


def readfile(filename):
    return np.loadtxt(filename, skiprows=3)


def do_weather():
    datafile = readfile("data.txt")

    tx_val = datafile[:, 6]  # Erdboden
    rr_val = datafile[:, 12]  # Niederschlagsmenge

    x = np.arange(start=0, stop=len(tx_val), step=1)

    real_point_list = [x, tx_val]

    points_of_num_Abl = get_num_Abl(real_point_list)
    points_of_ex_num_Abl = get_ex_num_Abl(points_of_num_Abl)

    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('Zeitpunkt')
    ax1.set_ylabel('Temp', color=color)
    ax1.plot(x, tx_val, 'r.')
    ax1.tick_params(axis='y', labelcolor=color)

    plt.show()


if __name__ == '__main__':
    zero_pointer = [1, 0, 0]
    function = np.poly1d(zero_pointer)

    points_of_fun = get_points_of_function(sin, 0.001, -10, 10)
    points_of_num_Abl = get_num_Abl(points_of_fun)
    #points_of_ex_num_Abl = get_ex_num_Abl(points_of_num_Abl)

    do_weather()

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(points_of_num_Abl[0], points_of_num_Abl[1])
    plt.show()
