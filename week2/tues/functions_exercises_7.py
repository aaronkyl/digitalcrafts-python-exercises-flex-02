import matplotlib
matplotlib.use("Agg")

from matplotlib import pyplot
from numpy import arange

def c_to_f(tempc):
    return (tempc * 9) / 5 + 32
    
if __name__ == "__main__":
    while True:
        try:
            tempc = float(input("Please enter a temperature in Celsius: "))
            break
        except ValueError:
            print("You did not enter a number. Please try one more time.")
    
    # x axis is celcius       
    xs = list(range(0, 100))
    # y axis is fahrenheit
    ys = []
    
    # user's data point
    xu = tempc
    yu = c_to_f(tempc)
    
    for x in xs:
        ys.append(c_to_f(x))
    
    pyplot.plot(xs, ys)
    pyplot.plot(xu, yu, 'ro')
    pyplot.savefig('funtions_exercises_7.png')
    pyplot.close()
    