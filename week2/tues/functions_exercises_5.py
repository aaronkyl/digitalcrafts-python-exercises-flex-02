import matplotlib
matplotlib.use("Agg")
import math

from matplotlib import pyplot
from math import sin

def f(x):
    return sin(x)

xs = list(range(-5, 6))
ys = []
for x in xs:
    ys.append(f(x))

pyplot.plot(xs, ys)
pyplot.savefig('funtions_exercises_5.png')
pyplot.close()