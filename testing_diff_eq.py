from prettytable import PrettyTable
import matplotlib.pyplot as plt
from Euler import euler_method
from Euler_Caushy import euler_caushy
from Runge_Kutta import runge_kutta
from linear_function import linear_function
from gauss_function import gauss_function
from quadratic_function import quadratic_function
from inter_appr import newton_interpolation, check_distance
import math


def comparison():
    #1
    eul = euler_method(["math.sin(x+y)"], [0], [0, 10], 100)[1]
    eul_cau = euler_caushy(["math.sin(x+y)"], [0], [0, 10], 100)
    rung = runge_kutta(["math.sin(x+y)"], [0], [0, 10], 100)

    mytable = PrettyTable()
    mytable.title = "y\' = math.sin(x+y)"
    mytable.add_column("i", [i[0] for i in eul])
    mytable.add_column("xi", [round(i[1], 2) for i in eul])
    mytable.add_column("Эйлер", [i[2] for i in eul])
    mytable.add_column("Эйлер-Коши", [i[2] for i in eul_cau])
    mytable.add_column("Рунге-Кутта", [i[2] for i in rung])
    print(mytable)

    x = [round(i[1], 2) for i in eul]
    y1 = [i[2] for i in eul]
    y2 = [i[2] for i in eul_cau]
    y3 = [i[2] for i in rung]

    # подготовка данных к МНК
    euler_mnk = [[x[i], y1[i]] for i in range(100)]
    euler_c_mnk = [[x[i], y2[i]] for i in range(100)]
    runge_mnk = [[x[i], y3[i]] for i in range(100)]

    plt.plot(x, y1, '-', label=f'Эйлер {quadratic_function(euler_mnk)[0]}')
    plt.plot(x, y2, '--', label=f'Эйлер-Коши {quadratic_function(euler_c_mnk)[0]}')
    plt.plot(x, y3, '-.', label=f'Рунге-Кутты {quadratic_function(runge_mnk)[0]}')
    plt.legend(loc='best')
    plt.grid()
    plt.show()


    print("Результат МНК для Эйлера:      ", quadratic_function(euler_mnk)[0])
    print("Результат МНК для Эйлера-Коши: ", quadratic_function(euler_c_mnk)[0])
    print("Результат МНК для Рунге-Кутты: ", quadratic_function(runge_mnk)[0])
    print("Интерполяция методом Ньтона для Эйлера:      ", newton_interpolation(euler_mnk)[0])
    print("Интерполяция методом Ньтона для Эйлера-Коши: ", newton_interpolation(euler_c_mnk)[0])
    print("Интерполяция методом Ньтона для Рунге-Кутты: ", newton_interpolation(runge_mnk)[0])



    #2
    eul = euler_method(["math.e**(-x) - y"], [1], [0, 1], 100)[1]
    eul_cau = euler_caushy(["math.e**(-x) - y"], [1], [0, 1], 100)
    rung = runge_kutta(["math.e**(-x) - y"], [1], [0, 1], 100)

    mytable = PrettyTable()
    mytable.title = "y\' = math.e**(-x) - y"
    mytable.add_column("i", [i[0] for i in eul])
    mytable.add_column("xi", [round(i[1], 2) for i in eul])
    mytable.add_column("Эйлер", [i[2] for i in eul])
    mytable.add_column("Эйлер-Коши", [i[2] for i in eul_cau])
    mytable.add_column("Рунге-Кутта", [i[2] for i in rung])
    print(mytable)

    x = [round(i[1], 2) for i in eul]
    y1 = [i[2] for i in eul]
    y2 = [i[2] for i in eul_cau]
    y3 = [i[2] for i in rung]
    func = [(math.e**(-i))*(i+1) for i in x]

    # подготовка данных к МНК
    euler_mnk = [[x[i], y1[i]] for i in range(100)]
    euler_c_mnk = [[x[i], y2[i]] for i in range(100)]
    runge_mnk = [[x[i], y3[i]] for i in range(100)]

    # График аппроксимацией квадратичной функцией
    plt.plot(x, y1, '-', label=f'Эйлер {quadratic_function(euler_mnk)[0]}')
    plt.plot(x, y2, '--', label=f'Эйлер-Коши {quadratic_function(euler_c_mnk)[0]}')
    plt.plot(x, y3, '-.', label=f'Рунге-Кутты {quadratic_function(runge_mnk)[0]}')
    plt.legend(loc='best')
    plt.grid()
    plt.show()

    print("Результат МНК для Эйлера:      ", quadratic_function(euler_mnk)[0])
    print("Результат МНК для Эйлера-Коши: ", quadratic_function(euler_c_mnk)[0])
    print("Результат МНК для Рунге-Кутты: ", quadratic_function(runge_mnk)[0])
    print("Интерполяция методом Ньтона для Эйлера:      ", newton_interpolation(euler_mnk)[0])
    print("Интерполяция методом Ньтона для Эйлера-Коши: ", newton_interpolation(euler_c_mnk)[0])
    print("Интерполяция методом Ньтона для Рунге-Кутты: ", newton_interpolation(runge_mnk)[0])

    # Результат линейной дисперсии для Эйлера:
    d1 = sum([abs(y1[i]-func[i]) for i in range(len(x))])
    print(f'Сигма для Эйлера = {d1}')

    # Результат линейной дисперсии для Эйлера-Коши:
    d2 = sum([abs(y2[i]-func[i]) for i in range(len(x))])
    print(f'Сигма для Эйлера-Коши = {d2}')

    # Результат линейной дисперсии для Рунге-Кутты:
    d3 = sum([abs(y3[i]-func[i]) for i in range(len(x))])
    print(f'Сигма для Рунге-Кутты = {d3}')


comparison()
