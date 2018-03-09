from turtle import *

def draw_octagon(thickness, pencolor, fillcolor):
    pensize(thickness)
    color(pencolor, fillcolor)
    begin_fill()
    for i in range(0, 8):
        forward(50)
        left(45)
    end_fill()
    
if __name__ == "__main__":
    draw_octagon(5, "black", "maroon")