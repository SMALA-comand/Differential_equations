from prettytable import PrettyTable
import matplotlib.pyplot as plt
from Euler import euler_method
from Euler_Caushy import euler_caushy
from Runge_Kutta import runge_kutta


def comparison():
    eul = euler_method(["math.sin(x+y)"], [0], [0, 1], 100)[1]
    eul_cau = euler_caushy(["math.sin(x+y)"], [0], [0, 1], 100)
    rung = runge_kutta(["math.sin(x+y)"], [0], [0, 1], 100)

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


comparison()
