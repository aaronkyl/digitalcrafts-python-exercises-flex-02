from turtle import *

def draw_star(thickness, pencolor, fillcolor):
    pensize(thickness)
    color(pencolor, fillcolor)
    left(35)
    begin_fill()
    for i in range(0, 5):
        forward(50)
        right(72)
        forward(50)
        left(144)
    end_fill()
    
if __name__ == "__main__":
    draw_star(5, "black", "gold")