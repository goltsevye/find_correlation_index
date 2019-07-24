import numpy as np
import matplotlib.pyplot as plt
import cmath
import math

fixed_row_Xr_Xi=[]

def create_x(x1, xn, xshift):
    while x1 <= xn:
        fixed_row_Xr_Xi.append(x1)
        x1 += xshift
    return fixed_row_Xr_Xi

Yr=[]

def create_yr(yr1, yrn, yrshift): # создает лист Yr
    while yr1 <= yrn:
        Yr.append(yr1)
        yr1 += yrshift
    return Yr

def check_size(fixed_row_Xr_Xi, Yr):
    if len(fixed_row_Xr_Xi) != len(Yr):
        print('неверно указаны размеры для листов')
        print(len(fixed_row_Xr_Xi), 'и', len(Yr))
    else: 
        return 0

create_x(-20, 20, 1) # задаем начало х, конец х и шаг
create_yr(-10, 10, 0.5) # задаем начало yr, конец yr и шаг
check_size(fixed_row_Xr_Xi, Yr) # проверка размеров созданных листов

Y_avg = 0
Yi=[]
overall = []
size_Yr = len(Yr)

def complexcorrel_linear(xs, ys, y2s, Y_avg):
    x_complex = []
    y_complex = []
    x_powered_sum = 0
    y_powered_sum = 0
    yx_sum = 0

    for x, y, y2 in zip(xs, ys, y2s):  # To complex , аргументы - fixed_row_Xr_Xi, Yr, Yi
        comp = complex(x, x)
        x_complex.append(comp)
        yi_avg = y2 - Y_avg
        comp = complex(y, yi_avg)
        y_complex.append(comp)
    for x, y in zip(x_complex, y_complex):  # To YX
        yx = np.multiply(x, y)
        yx_sum += yx
        x2 = (abs(x)) ** 2 * (math.cos(2 * (cmath.phase(x))) + math.sin(2 * cmath.phase(x)) * 1j)
        x_powered_sum += x2
        y2 = (abs(y)) ** 2 * (math.cos(2 * (cmath.phase(y))) + math.sin(2 * cmath.phase(y)) * 1j)
        y_powered_sum += y2
    sqrt_sumx_sumy = cmath.sqrt((x_powered_sum * y_powered_sum))
    correl = yx_sum / sqrt_sumx_sumy
    overall.append(correl)
    
    return round(correl, 4)
    #return correl       # показать коэф-т без округления


def create_graph(x, y, text):  # аргументы функции - значения Yr , Yi, название функции

    fig = plt.figure()
    ax = fig.add_subplot(111)

    x = Yr
    y = Yi
    ax.plot(x, y, 'red')    # для линии
    ax.set_xlabel('Yr')
    ax.yaxis.set_label_position('left')
    ax.set_ylabel('Yi')
    plt.grid(True)
    plt.text(3, 0, text)
    plt.title(complexcorrel_linear(fixed_row_Xr_Xi, Yr, Yi, Y_avg))
    #plt.scatter(x, y, color='red')  # для точечной диаграммы

    #return plt.savefig(text, format='png')  # сохраняет построенный график
    return plt.show()  # показывает построенный график


def sin_func():
    Y_avg = np.average(Yi)
    text = 'функция Yi = %dsin(Yr)' % k
    print(text)
    print('коэф-т  = ', complexcorrel_linear(fixed_row_Xr_Xi, Yr, Yi, Y_avg))
    create_graph(Yr, Yi, text)


for k in range(1, 2, 1):
    Yi=[]

    for p in range(0, size_Yr, 1):
        y = k*math.sin(Yr[p])
        Yi.append(y)
    
    sin_func()

print(Y_avg)

print(size_Yr)