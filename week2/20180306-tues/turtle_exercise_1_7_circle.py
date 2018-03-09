from turtle import *

def draw_circle(thickness, pencolor, fillcolor):
    pensize(thickness)
    color(pencolor, fillcolor)
    begin_fill()
    circle(50)
    end_fill()
    
if __name__ == "__main__":
    draw_circle(5, "black", "green")