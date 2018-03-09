import matplotlib
matplotlib.use("Agg")
import math

from matplotlib import pyplot
from math import sin
from numpy import arange

def f(x):
    return sin(x)

xs = list(arange(-5, 6, 0.1))
ys = []
for x in xs:
    ys.append(f(x))

pyplot.plot(xs, ys)
pyplot.savefig('funtions_exercises_6.png')
pyplot.close()