import random
import math


def zerodiv(fun):
    count = 0
    for j in range(20):
        x = random.randint(-100001, 100001)
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
    for j in range(20):
        x = random.randint(-100001, 100001)
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
    Ввод для дифференциального уравнение I порядка вида: y'=f(x,y)
    Начальное условие вида: y(0) = ... | x ∈ [...]
    Точность задаётся целым числом
    :return: f(x,y) | y(0) | x∈[a, b] | точность(n)
    """

    flag = False
    while not flag:
        func, a, b, n, y0 = [None] * 5

        # 1-ый блок, вводим функцию
        while func is None:
            fun = input('Введите функцию f(x, y): ')
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
            alphabet0 = ['b', 'd', 'f', 'j', 'k', 'q', 'r', 'u', 'v', 'w', 'z', 'z']
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
            else:  # сюда заходим, если for закончился без break
                x, y = 1, 1  # проверяем zeroDiv, синтаксис, ошибку вызову мат функций, ошибку значений мат функций
                flag_2 = False
                try:
                    eval(fun)
                except (SyntaxError, NameError):
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
                    func = fun

        # 2-ой блок, здесь будет ввод начальных условий
        while y0 is None:
            try:
                y_0 = float(input('\nВведите y(0): '))
            except ValueError:
                print('Введите значение в правильном формате!')
                continue

            y0 = y_0

        while a is None or b is None:
            try:
                aa, bb = map(float, input('\nВведите 2 числа через пробел - начало и конец отрезка.'
                                          '\nКонцы включены. Разделитель целой и дробной части - точка').split())
            except ValueError:
                print('Введите значения в правильном формате!')
                continue

            a, b = aa, bb

        # 3-ий блок, здесь будет ввод точности
        while n is None:
            try:
                s = int(input('\nВведите число n в ряде x0, x1, ..., xn: '))
            except ValueError:
                print('Введите значение в правильном формате!')
                continue
            if s <= 0:
                print('Шаг не может быть <= 0')
                continue
            else:
                n = s

        print('\nЕсли вы согласны с введёнными значениями и хотите завершить ввод, впишите любой символ/слово')
        print('В противном случае, напишите "NO" и вы начнёте с первого шага')
        check_input = input()
        if check_input != 'NO':
            return func, y0, [a, b], n
        elif check_input.lower() == 'no':
            continue


if __name__ == '__main__':
    print(diff_input())
