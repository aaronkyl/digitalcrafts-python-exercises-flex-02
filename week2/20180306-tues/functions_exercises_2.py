import matplotlib
matplotlib.use("Agg")

from matplotlib import pyplot

def f(x):
    return x + 1

xs = list(range(-3, 4))
ys = []
for x in xs:
    ys.append(f(x))

pyplot.plot(xs, ys)
pyplot.savefig('funtions_exercises_2.png')
pyplot.close()