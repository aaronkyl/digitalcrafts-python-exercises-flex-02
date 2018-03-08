from turtle import *

def draw_hexagon(thickness, pencolor, fillcolor):
    pensize(thickness)
    color(pencolor, fillcolor)
    begin_fill()
    for i in range(0, 6):
        forward(100)
        left(60)
    end_fill()
    
if __name__ == "__main__":
    draw_hexagon(5, "black", "maroon")