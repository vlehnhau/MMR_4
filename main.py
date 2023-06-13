import matplotlib.pyplot as plt
import numpy as np
import numpy.polynomial.polynomial as poly
from math import *


# Aufgabe 4.1.1
# a)

# Hier 2x^3 + 3x^2 - 4x + 1
# coe = [2, 3, -4, 1]
# coeAbl = [6, 6, -4]

# #print(np.poly1d(coe))

# start = -10
# stop = 10
# num = 100

# x_values = np.linspace(start, stop, num)
# y_values = np.polyval(coe, x_values)
# y_valuesAbl = np.polyval(coeAbl, x_values)

# step_size = (stop - start) / (num - 1)

# Ausgabe der berechneten Werte
# #print("Function")
# for x, y in zip(x_values, y_values):
#    #print(f"Für x = {x:.2f} ist y = {y:.2f}")


# numerische Ableitung

# def num_Abl(y_val, h):
#    return (y_val[2:] - y_val[:-2]) / (2 * h)


# nAbl = num_Abl(y_values, step_size)

# #print("Ableitung")
# for x, y in zip(nAbl, y_values):
#    #print(f"Für x = {x:.2f} ist y = {y:.2f}")

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


def get_num_Abl2(point_list):
    return_val = [[], []]
    step_size = point_list[0][1] - point_list[0][0]
    y_val = np.array(point_list[1])
    return_val[0] = point_list[0][:-1]
    return_val[1] = (y_val[1:] - y_val[:-1]) / step_size

    return return_val


def get_ex_num_Abl(point_list, real_points):
    prev_point = point_list[1][0]

    min = [[], []]
    max = [[], []]

    for i in range(1, len(point_list[0])):
        if prev_point >= 0 and point_list[1][i] < 0:
            min[0].append(point_list[0][i])
            min[1].append(real_points[1][i])
        if prev_point < 0 and point_list[1][i] >= 0:
            max[0].append(point_list[0][i])
            max[1].append(real_points[1][i])
        prev_point = point_list[1][i]

    return [min, max]


def sin1(x):
    return sin(1 / x)


def readfile(filename):
    return np.loadtxt(filename, skiprows=3)


def do_weather():
    datafile = readfile("data.txt")

    tx_val = datafile[:, 6]  # Erdboden

    x = np.arange(start=0, stop=len(tx_val), step=1)

    real_point_list = [x, tx_val]

    fun = np.poly1d(np.polyfit(real_point_list[0], real_point_list[1], 5))

    points_of_fun = get_points_of_function(fun, 1, 0, 500)
    points_of_num_Abl = get_num_Abl(points_of_fun)
    points_of_ex_num_Abl = get_ex_num_Abl(points_of_num_Abl, points_of_fun)

    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('Zeitpunkt')
    ax1.set_ylabel('Temp', color=color)
    ax1.plot(points_of_fun[0], points_of_fun[1], color=color)
    # ax1.plot(points_of_ex_num_Abl[0][0], points_of_ex_num_Abl[0][1], 'g.')
    # ax1.plot(points_of_ex_num_Abl[1][0], points_of_ex_num_Abl[1][1], 'g.')
    ax1.plot(x, tx_val, 'b.')
    ax1.tick_params(axis='y', labelcolor=color)

    plt.show()


def do_weathertwo():
    datafile = readfile("data.txt")

    y = datafile[:, 6]  # Erdboden
    x = np.arange(start=0, stop=len(y), step=1)
    h = 20

    new_x = []
    func_list = []

    for i in range(len(y)):
        new_x.append(i)

        if (i - h // 2) < 0:
            start = 0
        else:
            start = i - h // 2

        if i + h // 2 > len(y):
            end = len(y) - 1
        else:
            end = i + h // 2

        func_list.append(np.poly1d(np.polyfit(x[start:end], y[start:end], 5)))

    new_y = []

    for i, (func, j) in enumerate(zip(func_list, x)):
        y = func(j)
        new_y.append(y)

    points_of_fun_fake = [new_x, new_y]

    fun = np.poly1d(np.polyfit(points_of_fun_fake[0], points_of_fun_fake[1], 5))

    points_of_fun = get_points_of_function(fun, 1, 0, 500)
    points_of_num_Abl = get_num_Abl(points_of_fun)
    points_of_ex_num_Abl = get_ex_num_Abl(points_of_num_Abl, points_of_fun)

    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('Zeitpunkt')
    ax1.set_ylabel('Temp', color=color)
    ax1.plot(points_of_fun[0], points_of_fun[1], color=color)
    # ax1.plot(points_of_ex_num_Abl[0][0], points_of_ex_num_Abl[0][1], 'g.')
    # ax1.plot(points_of_ex_num_Abl[1][0], points_of_ex_num_Abl[1][1], 'g.')
    ax1.plot(x, datafile[:, 6], 'b.')
    ax1.tick_params(axis='y', labelcolor=color)

    plt.show()


if __name__ == '__main__':
    zero_pointer = [0.5, -3, 5, -2, 0.5]
    function = np.poly1d(zero_pointer)

    points_of_fun = get_points_of_function(function, 0.001, -100, 100)
    points_of_num_Abl = get_num_Abl(points_of_fun)
    points_of_num_Abl2 = get_num_Abl2(points_of_fun)

    points_of_ex_num_Abl = get_ex_num_Abl(points_of_num_Abl, points_of_fun)

    real_abl = np.poly1d([2, -9, 10, -2])
    x = np.linspace(-100, 100, 1000)
    y = real_abl(x)

    fig, ax1 = plt.subplots()
    plt.autoscale(False)
    plt.xlim([-10, 10])
    plt.ylim([-10, 10])
    ax1.plot(points_of_fun[0], points_of_fun[1], 'r')
    ax1.plot(points_of_num_Abl[0], points_of_num_Abl[1], 'b')
    ax1.plot(points_of_num_Abl2[0], points_of_num_Abl2[1], 'g')
    ax1.plot(x, y, 'y')
    ax1.plot(points_of_ex_num_Abl[0][0], points_of_ex_num_Abl[0][1], 'r.')
    ax1.plot(points_of_ex_num_Abl[1][0], points_of_ex_num_Abl[1][1], 'r.')
    plt.show()

    points_of_fun = get_points_of_function(sin, 0.001, -10, 10)
    points_of_num_Abl = get_num_Abl(points_of_fun)

    x = np.linspace(-100, 100, 1000)
    y = np.cos(x)

    fig, ax1 = plt.subplots()
    plt.autoscale(False)
    plt.xlim([-10, 10])
    plt.ylim([-10, 10])
    ax1.plot(points_of_fun[0], points_of_fun[1], 'r')
    ax1.plot(points_of_num_Abl[0], points_of_num_Abl[1], 'g')
    ax1.plot(x, y, 'y')
    plt.show()

    points_of_fun = get_points_of_function(sin1, 0.001, -10, 10)
    points_of_num_Abl = get_num_Abl(points_of_fun)

    x = np.linspace(-100, 100, 1000)
    y = -np.cos(1 / x) / (x ** 2)

    fig, ax1 = plt.subplots()
    plt.autoscale(False)
    plt.xlim([-10, 10])
    plt.ylim([-10, 10])
    ax1.plot(points_of_fun[0], points_of_fun[1], 'r')
    ax1.plot(points_of_num_Abl[0], points_of_num_Abl[1], 'g')
    ax1.plot(x, y, 'y')
    plt.show()

    do_weather()

    do_weathertwo()
