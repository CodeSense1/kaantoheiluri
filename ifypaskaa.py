
"""
A tool used to visualize

"""
import numpy as np
import matplotlib.pyplot as plt

import scipy.stats as sp
import csv
from math import sin, acos, sqrt, pi

# Initialize constant values here

# FILE = "mittaus.csv"
# U = 9.4  # V
# I = 3.2  # A
# P = U * I  # W

# deltat = 10 * 60

# M1 = 0.22386  # kg
# M2 = 0.3376  # kg

# degreeSign = u'\N{DEGREE SIGN}'

# aluminum = 0.896  # Kj/(kg*K)


def readData(file, delimiter=";"):
    """ Reads data from inputfile. Different measures must be separated by '#' sign
        Also '#' must be at the end of the file.

        param   file: Path to file you want to read
                delimiter: separator between values

        return: Yields values one by one, if your file has multiple values on same row
                they will be returned as a list

        For example:

        # mittaus1 (paikka/aika)
        0;0
        1;4
        2;8
        3;10
        # mittaus2 (nopeus/aika)
        14,0
        12;1
        10;2
        #
    """
    with open(file, newline="") as file:
        reader = csv.reader(file, delimiter=delimiter, dialect='excel')
        tmp = []
        for index, line in enumerate(reader):
            if "#" in line[0]:

                yield tmp
                tmp = []
                continue

            tmp.append(line)


def transform3D(data):

    x = []
    y = []
    z = []

    try:
        for i, j, k in data:
            i = i.replace(",", ".")
            j = j.replace(",", ".")
            k = k.replace(",", ".")

            x.append(float(i))
            y.append(float(j))
            z.append(float(k))

        return x, y, z

    except ValueError:
        print("Invalid data: {}, {}, {}".format(z, y, z))


def transform2D(data):
    """
    Transform 2d array to two 1d lists
    :param 2d-array like
    :return two arrays (mA, V)
    """

    x = []
    y = []

    try:

        for i, j in data:
            i = i.replace(",", ".")
            j = j.replace(",", ".")

            # Add two values to list
            x.append(float(i))
            y.append(float(j))

        return x, y
    except ValueError:
        print("values {}, {} are not valid!".format(i, j))


def transform1D(data):
    """ 
    Transforms single measure points to list of floats
    """
    x = []
    try:

        for i in data:
            i = i[0].replace(',', '.')
            x.append(float(i))

        return x
    except ValueError:
        print(x, "is not valid number.")


def trendline(X, Y):
    """
    Returns estimated intercept and slope
    :param X;Y: list of values
    :return intercept, slope
    """

    # Scipy.stats, least square method
    slope, intercept, r, s, err = sp.linregress(X, Y)

    return slope, intercept


def angle(v1, v2):
    """ Angle between two vectors """
    tmp = dot(v1, v2) / (vlen(v1) * vlen(v2))
    return acos(tmp)


def dot(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1]


def vlen(v):
    """ lenght of a vector"""
    return sqrt(v[0]**2 + v[1]**2)


def tArea(vertex):
    """
    Returns area of a triangle
    :param vertex: 2d array-like, vertex points of triangle
    :return area of given triangle
    """

    p1, p2, p3 = vertex

    # Make two vectors
    v1 = [p1[0] - p2[0], p1[1] - p2[1]]
    v2 = [p3[0] - p2[0], p3[1] - p2[1]]

    a = angle(v1, v2)

    area = 0.5 * vlen(v1) * vlen(v2) * sin(a)

    return area


def example():
    FILE = "mittaus.csv"
    for n, measures in enumerate(readData(FILE)):

        U = 9.4  # V
        I = 3.2  # A
        P = U * I  # W

        deltat = 10 * 60

        M1 = 0.22386  # kg
        M2 = 0.3376  # kg

        degreeSign = u'\N{DEGREE SIGN}'

        aluminum = 0.896  # Kj/(kg*K)

        ################################################################
        # This is the main part. n represents the current measure.
        # Here is an example of visualization of  two processes.
        ################################################################

        # Read and modify data and store it to these values
        t, T = transform2D(measures)

        # Pienimassainen kappale
        if n == 1:
            fig = plt.figure(0, figsize=(7, 8))
            ax = plt.axes()
            plt.yticks(np.arange(25, 85, step=2.5))

            # Make trendlines
            lowX = np.linspace(0, 360, 5)
            lowY = T[:5]

            highX = t[-3:]
            highY = T[-3:]

            a, b = trendline(lowX, lowY)
            c, d = trendline(highX, highY)

            t1 = np.linspace(670, 1260, 100)
            t2 = np.linspace(0, 670, 100)

            lineX = np.ones(100) * 670
            lineY = np.linspace(29, 80, 100)

            plt.plot(lineX, lineY, ":")
            # Measure delta T

            dT1 = lineY[-1] - lineY[0]

            plt.xlabel("Aika (s)")
            plt.ylabel("Lämpötila (" + degreeSign + "C)")
            # initialize subplots

            plt.scatter(t, T, marker="x")
            plt.plot(t, T)

            plt.text(575, 60, r'$\Delta$T', fontsize=12)

            plt.plot(t1, c * t1 + d, "--")
            plt.plot(t2, a * t2 + b, "-.")
            plt.legend([r'$\Delta$T', "pääjakso", "jälkijakso", "esijakso"])
            plt.savefig("pieniMassa.png")
            plt.show()

        # Suurimassainen kappale
        if n == 2:
            fig = plt.figure(0, figsize=(7, 8))
            ax = plt.axes()
            plt.yticks(np.arange(25, 85, step=2.5))

            # Points for trendlines
            highX = t[-3:]
            highY = T[-3:]

            lowX = np.linspace(0, 360, 5)
            lowY = T[:5]

            # define trendlines
            a, b = trendline(highX, highY)
            c, d = trendline(lowX, lowY)

            # linspaces for lines
            t1 = np.linspace(673, 1260, 100)
            t2 = np.linspace(0, 673, 100)

            lineX = np.ones(100) * 673
            lineY = np.linspace(29, 66, 100)

            plt.plot(lineX, lineY, ":")

            # Measure delta T
            dT2 = lineY[-1] - lineY[0]

            plt.xlabel("Aika (s)")
            plt.ylabel("Lämpötila (" + degreeSign + "C)")
            plt.text(550, 50, r'$\Delta$T', fontsize=13)

            plt.plot(t1, a * t1 + b, "--")
            plt.plot(t2, c * t2 + d, "-.")
            plt.scatter(t, T, marker="x")
            plt.plot(t, T)
            plt.legend([r'$\Delta$T', "jälkijakso", "esijakso", "pääjakso"])
            plt.savefig("suurimassa.png")

            plt.show()

    # Q = cmdT
    # c = Q/(m*dT)

    # Alumiinin ominaislämpö - 900 j/kgK

    dt = (14 - 6) * 60
    print(dT1, dT2)
    # Pieni massa
    cM1 = P * dt / (M1 * dT1)
    print(cM1)
    # Suuri
    cM2 = P * dt / (M2 * dT2)
    print(cM2)

    # In[5]:

    c = (1 / (M1 - M2)) * ((P * deltat) / dT1 - ((P * deltat) / dT2))
    print(c)
