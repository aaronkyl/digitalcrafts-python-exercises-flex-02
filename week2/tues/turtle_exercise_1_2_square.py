from turtle import *

def draw_square(thickness, pencolor, fillcolor):
    pensize(thickness)
    color(pencolor, fillcolor)
    begin_fill()
    for i in range(0, 4):
        forward(100)
        left(90)
    end_fill()
    
if __name__ == "__main__":
    draw_square(5, "black", "yellow")