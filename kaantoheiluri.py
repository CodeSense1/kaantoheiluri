
from ifypaskaa import *
from statistics import stdev, mean

FILE = "kaantoheiluri.csv"
b1 = 35.9  # b1
b2 = 64.5  # b2


def difference(d1, d2):
    # Calculate difference between two datapoints
    diff = []

    for i, j in zip(d1, d2):
        diff.append(i - j)

    return diff


def g(t1, t2, b1, b2):
    temp = []

    for i, j in zip(t1, t2):
        print(i, j, i**2 * b1 - j**2 * b2)
        temp.append(4 * pi**2 * (b1**2 - b2**2) / (i**2 * b1 - j**2 * b2))

    return mean(temp)


for n, measures in enumerate(readData(FILE)):

    if n == 0:
        continue

    if n == 1:
        t = transform1D(measures)
        # calculating standart deviation of measure accuracy
        deviation = stdev(t)

    elif n == 2:
        l, t1, t2 = transform3D(measures)
        dt = difference(t1, t2)

        dx = np.linspace(70, 87, 100)
        xAxis = np.linspace(67, 87, 100)

        k, b = trendline(l, dt)

        zeroX = -b / k

        gravity = g(t1, t2, b1, b2)
        print(gravity)

        plt.scatter(l, dt)
        plt.plot(dx, k * dx + b, '--', color='g')
        plt.plot(xAxis, 0 * xAxis, color="black")
        plt.plot(zeroX - 0.1, 0, 'ro', markersize=7)

        plt.text(82, 0.2, "82,9cm")

        plt.xlabel("Pituus (cm)")
        plt.ylabel("Aikaero (s)")

        plt.legend(['aikaero T-T\' pituuden funktiona'])

        plt.show()
