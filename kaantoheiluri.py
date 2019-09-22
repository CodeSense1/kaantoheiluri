
from ifypaskaa import *
from statistics import stdev

FILE = "kaantoheiluri.csv"


for n, measures in enumerate(readData(FILE)):

    if n == 0:
        continue

    if n == 1:
        t = transform1D(measures)

        deviation = stdev(t)

    elif n == 2:
        t1, t2 = transform2D(measures)

        dx = np.linspace(95, 101, 100)

        k, b = trendline(t1, t2)

        plt.scatter(t1, t2)
        plt.plot(dx, k * dx + b, '--')
        plt.show()
