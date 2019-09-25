
from ifypaskaa import *
from statistics import stdev

FILE = "kaantoheiluri.csv"
b1 = 0.359  # b1
b2 = 0.645  # b2

t100 = 199.70
t101 = 200.03


def difference(d1, d2):
    # Calculate difference between two datapoints
    diff = []

    for i, j in zip(d1, d2):
        diff.append(i - j)

    return diff


def g(t1, t2, b1, b2):
    temp = []

    part1 = 4 * pi**2
    part2 = b1**2 - b2**2

    # for i, j in zip(t1, t2):
    part3 = (t1 / 100)**2 * b1 - (t2 / 100)**2 * b2

    return part1 * part2 / part3

    # return mean(temp)


for n, measures in enumerate(readData(FILE)):

    if n == 0:
        continue

    if n == 1:
        t = transform1D(measures)
        # calculating standart deviation of measure accuracy
        deviation = stdev(t)

    elif n == 2:
        # ##### Putoamiskiihtyvyyden selvittäminen ######
        # l, t1, t2 = transform3D(measures)
        # dt = difference(t1, t2)

        # dx = np.linspace(70, 87, 100)
        # xAxis = np.linspace(67, 87, 100)

        # k, b = trendline(l, dt)

        # zeroX = -b / k

        # gravity = g(t100, t101, b1, b2)
        # print(gravity)

        # plt.scatter(l, dt)
        # plt.plot(dx, k * dx + b, '--', color='g')
        # plt.plot(xAxis, 0 * xAxis, color="black")
        # plt.plot(zeroX - 0.1, 0, 'ro', markersize=7)

        # plt.text(82, 0.2, "82,9cm")

        # plt.xlabel("Pituus (cm)")
        # plt.ylabel("Aikaero (s)")

        # plt.legend(['aikaero T-T\' pituuden funktiona'])

        # plt.show()

        ##############################################
        ###### Karkea tasapainopisteen määritys ######
        ##############################################

        # DT = [-1.84, -1.15, -1.3, -0.04, 2.12]
        # d = [50, 60, 70, 80, 90]

        # plt.scatter(d, DT)
        # a, b = trendline(d, DT)

        # x = np.linspace(50, 95, 100)
        # plt.plot(x, a * x + b)
        # plt.plot(np.linspace(50, 90, 100), np.ones(100) * 0)

        # plt.text(73, 0.3, "74,96", fontsize=12)
        # plt.plot(74.96, 0, 'ro', markersize=12)

        # plt.legend(['Aikaero T-T\' ajan funktiona'])
        # plt.xlabel('T-T\'/s')
        # plt.ylabel('d/cm')
        # plt.title('Karkea tasapainopisteen määritys')

        # plt.savefig('tp.png')
        # plt.show()

        ###### Tarkempi tasapainopisteen haarukointi ######

        DT = [-2.85,
              -1.65,
              -1.1,
              -1.03,
              -0.88,
              -0.28,
              0.13
              ]
        d = [70.96,
             72.96,
             74.96,
             76.96,
             78.9,
             81.96,
             83.96
             ]

        plt.scatter(d, DT)
        a, b = trendline(d, DT)

        x = np.linspace(70, 90, 100)
        plt.plot(x, a * x + b)
        plt.plot(np.linspace(68, 90, 100), np.ones(100) * 0)

        zero = -b / a
        plt.text(zero - 1.5, 0.3, '82,9', fontsize=12)
        plt.plot(zero, 0, 'ro', markersize=12)

        plt.legend(['Aikaero T-T\' ajan funktiona'])
        plt.xlabel('T-T\'/s')
        plt.ylabel('d/cm')
        plt.title('Tarkempi tasapainopisteen määritys')

        # plt.savefig('tarkka-tp.png')
        plt.show()
