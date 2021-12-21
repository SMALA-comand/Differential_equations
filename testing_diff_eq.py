from prettytable import PrettyTable
import matplotlib.pyplot as plt
from Euler import euler_method
from Euler_Caushy import euler_caushy
from Runge_Kutta import runge_kutta
from linear_function import linear_function
from gauss_function import gauss_function
from quadratic_function import quadratic_function
from inter_appr import newton_interpolation, check_distance


def comparison():
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
    plt.plot(x, y1, '-', x, y2, '--', x, y3, '-.')
    plt.show()

    # подготовка данных к МНК
    euler_mnk = [[x[i], y1[i]] for i in range(100)]
    euler_c_mnk = [[x[i], y2[i]] for i in range(100)]
    runge_mnk = [[x[i], y3[i]] for i in range(100)]

    print("Результат МНК для Эйлера:      ", quadratic_function(euler_mnk)[0])
    print("Результат МНК для Эйлера-Коши: ", quadratic_function(euler_c_mnk)[0])
    print("Результат МНК для Рунге-Кутты: ", quadratic_function(runge_mnk)[0])

    print("Интерполяция методом Ньтона для Эйлера:      ", newton_interpolation(euler_mnk)[0])
    print("Интерполяция методом Ньтона для Эйлера-Коши: ", newton_interpolation(euler_c_mnk)[0])
    print("Интерполяция методом Ньтона для Рунге-Кутты: ", newton_interpolation(runge_mnk)[0])


comparison()
