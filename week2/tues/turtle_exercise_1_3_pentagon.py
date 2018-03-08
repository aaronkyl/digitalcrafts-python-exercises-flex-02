from turtle import *

def draw_pentagon(thickness, pencolor, fillcolor):
    pensize(thickness)
    color(pencolor, fillcolor)
    begin_fill()
    for i in range(0, 5):
        forward(100)
        left(72)
    end_fill()
    
if __name__ == "__main__":
    draw_pentagon(5, "black", "maroon")