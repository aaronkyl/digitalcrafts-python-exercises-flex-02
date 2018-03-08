from turtle import *

def draw_equilateral_triangle(thickness, pencolor, fillcolor):
    pensize(thickness)
    color(pencolor, fillcolor)
    begin_fill()
    for i in range(0, 3):
        forward(100)
        left(120)
    end_fill()
    
if __name__ == "__main__":
    draw_equilateral_triangle(5, "black", "maroon")