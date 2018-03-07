import matplotlib
matplotlib.use("Agg")

from matplotlib import pyplot

def f(x):
    # odd numbers
    if x % 2:
        return 1
    # even numbers
    else:
        return -1

xs = list(range(-5, 6))
ys = []
for x in xs:
    ys.append(f(x))

pyplot.bar(xs, ys)
pyplot.savefig('funtions_exercises_4.png')
pyplot.close()