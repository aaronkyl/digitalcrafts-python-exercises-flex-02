import matplotlib
matplotlib.use("Agg")

from matplotlib import pyplot

def f(x):
    return x * x

xs = list(range(-100, 101))
ys = []
for x in xs:
    ys.append(f(x))

pyplot.plot(xs, ys)
pyplot.savefig('funtions_exercises_3.png')
pyplot.close()