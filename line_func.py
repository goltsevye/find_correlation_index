import numpy as np
import matplotlib.pyplot as plt
import cmath
import math


fixed_row_Xr_Xi = [-20, -19, -18, -17, -16, -15, -14, -13, -12, -11,
                   -10, -9, -8, -7, -6, -5, -4, -3, -2, -1,
                   0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                   10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

Yr = [-10, -9.5, -9, -8.5, -8, -7.5, -7, -6.5, -6, -5.5,
      -5, -4.5, -4, -3.5, -3, -2.5, -2, -1.5, -1, -0.5,
      0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5,
      5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10]

Yi=[]
overall = []
size_Yr = len(Yr)


def complexcorrel_linear(xs, ys, y2s):
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
    
    return correl


def create_graph(x, y, text):  # аргументы функции - значения Yr , Yi, название функции

    fig = plt.figure()
    ax = fig.add_subplot(111)

    x = Yr
    y = Yi
    #ax.plot(x, y, 'red')    # для линии
    ax.set_xlabel('Yr')
    ax.yaxis.set_label_position('left')
    ax.set_ylabel('Yi')
    plt.grid(True)
    plt.text(3, 0, text)
    plt.title(complexcorrel_linear(fixed_row_Xr_Xi, Yr, Yi))
    plt.scatter(x, y, color='red')  # для точечной диаграммы

    #return plt.savefig(text, format='png')  # сохраняет построенный график
    return plt.show()  # показывает построенный график


for k in range(1,5,1): # задаем (начало, конец, шаг(целое число)) для k
    Yi=[]
    text = 0

    for b in range(0, 5, 1): # задаем (начало, конец, шаг(целое число)) для b
        Yi=[]
        text = 0

        for p in range(0,size_Yr, 1): 
            y = k*Yr[p] + b
            Yi.append(y)
        
        Y_avg = np.average(Yi)
        text = 'функция Yi = %dYr + %d' % (k, b)
        print(text)
        print('коэф-т  = ', complexcorrel_linear(fixed_row_Xr_Xi, Yr, Yi))
        create_graph(Yr, Yi, text)