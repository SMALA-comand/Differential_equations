from Euler import euler_method
import math


def euler_caushy(function=None, y0=None, a_b=None, n=None):
    if function is None or y0 is None or a_b is None or n is None:
        euler = euler_method()
        function = euler[0]
        table_euler = euler[1]

        # восстанавливаем значение h, [a, b], y0, x0 из table_euler
        # имеем массив [(i, yi, xi), ...]

        a = table_euler[0][2]
        b = table_euler[-1][2]
        n = len(table_euler)-1
        h = (b-a)/n

        y0 = table_euler[0][1]
        x0 = a
    else:
        table_euler = euler_method(function, y0, a_b, n)[1]
        a, b = a_b
        h = (b - a) / n
        x0 = a

    answer_list = [(0, y0, x0)]
    for i in range(1, n+1):
        y = y0
        x = x0
        f_xy = eval(function)

        x = x0+h
        y = table_euler[i][2]
        f_xy_dop = eval(function)

        yi = y0 + (h/2) * (f_xy + f_xy_dop)
        y0 = yi
        x0 = x0+h
        answer_list.append((i, yi, x0))

    return answer_list


if __name__ == "__main__":
    print(euler_caushy())

