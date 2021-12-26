"""
``DifferentialEquations.DiffEq``
================================

Модуль, реализующий решения дифференциальных уравнений.
В данный момент поддерживаются алгоритмы: Эйлера, Эйлера Коши, Рунге-Кутты

"""
import random
import math
from copy import deepcopy

__all__ = ['euler_method', 'euler_caushy', 'runge_kutta']

def zerodiv(fun):
    count = 0
    for j in range(30):
        x, y, z, u, v = [random.randint(-100001, 100001)] * 5
        try:
            eval(fun)
        except ZeroDivisionError:
            count += 1
        except ValueError:
            continue
    if count == 20:
        return True
    return False


def valuer(fun):
    count = 0
    for j in range(30):
        x, y, z, u, v = [random.randint(-100001, 100001)] * 5
        try:
            eval(fun)
        except ValueError:
            count += 1
        except ZeroDivisionError:
            continue
    if count == 20:
        return True
    return False


def diff_input():
    """
    Ввод для дифференциального уравнение I порядка вида: y'=f(x,y) или систем таких уравнений
    Либо для ДУ II порядка вида: y'=f(x,y,y')
    Начальное условие вида: y(m) = ... | x ∈ [m, ...]
    Точность задаётся целым числом
    :return: [f(x,y,...),...] | [y(0), z[0],...] | x∈[a, b] | точность(n)
    """

    flag = False
    while not flag:
        system = None
        print('Введите кол-во уравнений в системе (от 1 до 4): ')
        while system is None:
            try:
                count = int(input('Количество уравнений: '))
            except ValueError:
                print('Введите значение в правильном формате!')
                continue
            system = count

        mode = None
        if system == 1:
            print('Для систем из 1 уравнения предусмотрена возможность ввести ДУ 1-ого/2-ого порядка на выбор')
            while mode is None:
                try:
                    digit = int(input('Порядок уравнения: '))
                except ValueError:
                    print('Введите значение в правильном формате!')
                    continue
                mode = digit

        if mode == 2:
            fun = input('Введите функцию: ')
            fun = fun.lower()
            fun = fun.replace("y\'", "z")

        func1, func2, func3, func4 = [None] * 4
        y0, z0, u0, v0 = [None] * 4
        if mode == 2:
            for_func = ['z', fun]
        else:
            for_func = [func1, func2, func3, func4]

        for_yzuv = [y0, z0, u0, v0]
        a, b, n = [None] * 3

        # 1-ый блок, вводим функцию
        func_string = ['y', 'z', 'u', 'v']
        string = ', '.join(func_string[0:system])
        answer_func = []
        if mode == 2:
            system = mode

        for i in range(0, system):
            func = for_func[i]
            c = 0
            while func is None or (mode == 2 and c == 0):
                if mode != 2:
                    fun = input(f'Введите функцию d{func_string[i]}/dx = f(x, {string}): ')
                else:
                    fun = func

                if '^' in fun:
                    fun = fun.replace('^', '**')
                fun = fun.lower()

                plan = ['e', 'pi', 'sin', 'cos', 'tan', 'log']
                dict_replace = {i: 'math.' + i for i in plan}
                dict_replace['tg'] = 'math.tan'
                dict_replace['ln'] = 'math.log'
                dict_replace['ctan'] = '1/math.tan'
                dict_replace['ctg'] = '1/math.tan'

                for item in dict_replace:
                    if item in fun:
                        fun = fun.replace(item, dict_replace[item])

                # проверяем есть ли лишние буквы
                alphabet0 = ['z', 'u', 'v', 'j', 'k', 'q', 'r', 'b', 'd', 'w', 'f', 'f']
                for j in range(0, system-1):
                    alphabet0[j] = 'j'
                alphabet1 = ['t', 'a', 'p', 'i', 's', 'n', 'c', 'o', 'l', 'g', 'h', 'm']
                alphabet2 = {
                    't': ['math', 'tan'], 'a': ['math', 'tan'], 'p': ['pi'], 'i': ['sin', 'pi'],
                    's': ['sin', 'cos'], 'n': ['tan', 'sin'], 'c': ['cos'], 'o': ['cos', 'log'],
                    'l': ['log'], 'g': ['log'], 'h': ['math'], 'm': ['math']
                }

                for letter in range(len(alphabet0)):
                    if alphabet0[letter] in fun:
                        print('У вас есть лишние переменные/символы букв')
                        break
                    let = alphabet1[letter]
                    if fun.count(let) > sum(list(map(lambda x: fun.count(x), alphabet2[let]))):
                        print('У вас есть лишние переменные/символы букв')
                        break
                else:   # сюда заходим, если for закончился без break
                    x, y, z, u, v = [1] * 5     # проверяем ошибки при вызове eval()
                    flag_2 = False
                    try:
                        eval(fun)
                    except (SyntaxError, NameError, AttributeError):
                        print('Синтаксическая ошибка!')
                        flag_2 = True
                    except ValueError:
                        if valuer(fun):
                            print('Скорее всего в вашей формуле статическая ошибка в логарифме, исправьте её')
                            flag_2 = True
                    except ZeroDivisionError:
                        if zerodiv(fun):
                            print('Скорее всего в вашей формуле статическое деление на ноль')
                            flag_2 = True
                    except TypeError:
                        print('Неправильное использование мат. функций (проверьте ваши логарифмы и триг. ф-ции)')
                        flag_2 = True

                    if flag_2:
                        func = None
                    if not flag_2:
                        answer_func.append(fun)
                        func = fun
                        c = 1

        if mode == 2:
            print('Ваше уравнение было превращено в систему: ')
            print("{" + f'y\' = {answer_func[0]}')
            print("{" + f'z\' = {answer_func[1]}')

        # 2-ой блок, здесь будет ввод начальных условий
        while a is None or b is None:
            try:
                aa, bb = map(float, input('\nВведите 2 числа через пробел - начало и конец отрезка.'
                                          '\nКонцы включены. Разделитель целой и дробной части - точка').split())
            except ValueError:
                print('Введите значения в правильном формате!')
                continue

            a, b = aa, bb

        answer_yzuv = []
        for i in range(0, system):
            yzuv = for_yzuv[i]
            while yzuv is None:
                try:
                    some_func = float(input(f'\nВведите {func_string[i]}({a}): '))
                except ValueError:
                    print('Введите значение в правильном формате!')
                    continue
                yzuv = some_func
                answer_yzuv.append(yzuv)

        # 3-ий блок, здесь будет ввод точности
        while n is None:
            try:
                s = int(input('\nВведите число n в ряде x0, x1, ..., xn: '))
            except ValueError:
                print('Введите значение в правильном формате!')
                continue
            if s <= 0:
                print('Количество не может быть <= 0')
                continue
            else:
                n = s

        print('\nЕсли вы согласны с введёнными значениями и хотите завершить ввод, впишите любой символ/слово')
        print('В противном случае, напишите "NO" и вы начнёте с первого шага')
        check_input = input()
        if check_input != 'NO':
            return answer_func, answer_yzuv, [a, b], n
        elif check_input.lower() == 'no':
            continue


if __name__ == '__main__':
    print(diff_input())


def euler_method(function=None, yzuv=None, a_b=None, n=None):
    """
     Решение уравнение методом Эйлера
     :param function: Вводимая функция
     :param yzuv: Значение функции в точке y(0)
     :param a_b: Промежуток на котором решаем диф. уравнение
     :param n: Точность, которая задаётся целым числом
     :return: function, answer_list
     """
    if function is None or yzuv is None or a_b is None or n is None:
        function, yzuv, a_b, n = diff_input()

    a, b = a_b
    h = (b-a)/n
    x0 = a

    answer_list = [(0, x0, *yzuv)]
    g = len(yzuv)
    while len(yzuv) < 4:
        yzuv.append(None)

    yi, zi, ui, vi = [None] * 4
    f1, f2, f3, f4 = [None] * 4
    k = [yi, zi, ui, vi]
    f = [f1, f2, f3, f4]

    for i in range(1, n+1):
        x, y, z, u, v = x0, *yzuv

        for j in range(0, g):
            f_xy = eval(function[j])
            f[j] = h * f_xy
            k[j] = yzuv[j] + f[j]
            yzuv[j] = k[j]

        x0 += h

        answer_list.append((i, x0, *k[0:g]))

    return function, answer_list


if __name__ == "__main__":
    print(euler_method())


def euler_caushy(function=None, yzuv=None, a_b=None, n=None):
    """
         Решение уравнение методом Эйлера-Коши
         :param function: Вводимая функция
         :param yzuv: Значение функции в точке y(0)
         :param a_b: Промежуток на котором решаем диф. уравнение
         :param n: Точность, которая задаётся целым числом
         :return: answer_list
         """
    if function is None or yzuv is None or a_b is None or n is None:
        euler = euler_method()
        function = euler[0]
        table_euler = euler[1]
    else:
        table_euler = euler_method(function, yzuv, a_b, n)[1]

    a = table_euler[0][1]
    b = table_euler[-1][1]
    n = len(table_euler) - 1
    h = (b - a) / n

    yzuv = table_euler[0][2:]
    yzuv = list(yzuv)
    x0 = a

    answer_list = [(0, x0, *yzuv)]
    g = len(yzuv)
    while len(yzuv) < 4:
        yzuv.append(None)

    f1, f2, f3, f4 = [None] * 4
    f = [f1, f2, f3, f4]
    new_f1, new_f2, new_f3, new_f4 = [None] * 4
    new_f = [new_f1, new_f2, new_f3, new_f4]
    yi, zi, ui, vi = [None] * 4
    k = [yi, zi, ui, vi]

    for i in range(1, n+1):
        x, y, z, u, v = x0, *yzuv

        for j in range(g):
            f[j] = eval(function[j])

        new_yzuv = yzuv
        new_yzuv[0:g] = table_euler[i][2:]
        x, y, z, u, v = x0+h, *new_yzuv
        for j in range(g):
            new_f[j] = eval(function[j])

        for j in range(g):
            k[j] = yzuv[j] + (h/2) * (f[j] + new_f[j])
            yzuv[j] = k[j]

        x0 += h
        answer_list.append((i, x0, *k[0:g]))

    return answer_list


if __name__ == "__main__":
    print(euler_caushy())


def runge_kutta(function=None, yzuv=None, a_b=None, n=None):
    """
     Решение уравнение методом Рунге-Кутты
     :param function: Вводимая функция
     :param yzuv: Значение функции в точке y(0)
     :param a_b: Промежуток на котором решаем диф. уравнение
     :param n: Точность, которая задаётся целым числом
     :return: answer_list
     """
    if function is None or yzuv is None or a_b is None or n is None:
        function, yzuv, a_b, n = diff_input()

    a, b = a_b
    h = (b-a)/n
    x0 = a

    answer_list = [(0, x0, *yzuv)]
    g = len(yzuv)
    while len(yzuv) < 4:
        yzuv.append(None)

    yi, zi, ui, vi = [None] * 4
    func_i = [yi, zi, ui, vi]
    k_i = [[None] * 4 for i in range(g)]
    for i in range(1, n+1):
        for j in range(0, g):
            x, y, z, u, v = x0, *yzuv
            f_xy = eval(function[j])
            k_i[j][0] = h * f_xy

        new_yzuv = deepcopy(yzuv)
        new_yzuv[0:g] = [(yzuv[j] + k_i[j][0]/2) for j in range(g)]
        for j in range(0, g):
            x, y, z, u, v = x0 + h/2, *new_yzuv
            f_xy = eval(function[j])
            k_i[j][1] = h * f_xy

        new_yzuv = deepcopy(yzuv)
        new_yzuv[0:g] = [(yzuv[j] + k_i[j][1] / 2) for j in range(g)]
        for j in range(0, g):
            x, y, z, u, v = x0 + h/2, *new_yzuv
            f_xy = eval(function[j])
            k_i[j][2] = h * f_xy

        new_yzuv = deepcopy(yzuv)
        new_yzuv[0:g] = [(yzuv[j] + k_i[j][2]) for j in range(g)]
        for j in range(0, g):
            x, y, z, u, v = x0 + h, *new_yzuv
            f_xy = eval(function[j])
            k_i[j][3] = h * f_xy

        for j in range(g):
            func_i[j] = yzuv[j] + (1/6)*(k_i[j][0] + 2*k_i[j][1] + 2*k_i[j][2] + k_i[j][3])
            yzuv[j] = func_i[j]

        x0 += h
        answer_list.append((i, x0, *func_i[0:g]))

    return answer_list


if __name__ == "__main__":
    print(runge_kutta(["math.sin(x+y)"], [0], [0, 1], 10))