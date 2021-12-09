from differential_input import diff_input
import math


def euler_method(function=None, y0=None, a_b=None, n=None):
    if function is None or y0 is None or a_b is None or n is None:
        function, y0, a_b, n = diff_input()

    a, b = a_b
    h = (b-a)/n
    x0 = a

    answer_list = [(0, y0, x0)]
    for i in range(1, n+1):
        y = y0
        x = x0
        f_xy = eval(function)
        yi = y0 + h*f_xy
        y0 = yi
        x0 = x+h
        answer_list.append((i, yi, x0))

    return function, answer_list


if __name__ == "__main__":
    print(euler_method())
