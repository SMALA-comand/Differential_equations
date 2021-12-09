from differential_input import diff_input
import math


def runge_kutta(function=None, y0=None, a_b=None, n=None):
    if function is None or y0 is None or a_b is None or n is None:
        function, y0, a_b, n = diff_input()

    a, b = a_b
    h = (b-a)/n
    x0 = a

    answer_list = [(0, y0, x0)]
    for i in range(1, n+1):
        x = x0
        y = y0
        f_xy = eval(function)
        k1 = h * f_xy

        x = x0 + h/2
        y = y0 + k1/2
        f_xy = eval(function)
        k2 = h * f_xy

        x = x0 + h / 2
        y = y0 + k2 / 2
        f_xy = eval(function)
        k3 = h * f_xy

        x = x0 + h
        y = y0 + k3
        f_xy = eval(function)
        k4 = h * f_xy

        yi = y0 + (1/6) * (k1 + 2*k2 + 2*k3 + k4)
        x0 = x0 + h
        y0 = yi

        answer_list.append((i, yi, x0))

    return answer_list


if __name__ == "__main__":
    print(runge_kutta())
