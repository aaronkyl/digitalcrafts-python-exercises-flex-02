from turtle import *

def draw_shape(shape, thickness, sidelength, fill=False, pen_color="black", fill_color=None):
    pensize(thickness)
    down()
    pencolor(pen_color)
    if fill:
        fillcolor(fill_color)
        begin_fill()
    if shape == "triangle":
        for i in range(0, 3):
            forward(sidelength)
            left(120)
    elif shape == "square":
        for i in range(0, 4):
            forward(sidelength)
            left(90)
    elif shape == "pentagon":
        for i in range(0, 5):
            forward(sidelength)
            left(72)
    elif shape == "hexagon":
        for i in range(0, 6):
            forward(sidelength)
            left(60)
    elif shape == "octagon":
        for i in range(0, 8):
            forward(sidelength)
            left(45)
    elif shape == "star":
        left(35)
        for i in range(0, 5):
            forward(sidelength)
            right(72)
            forward(sidelength)
            left(144)
    elif shape == "circle":
        circle(sidelength)
    else:
        home()
    end_fill()
    up()