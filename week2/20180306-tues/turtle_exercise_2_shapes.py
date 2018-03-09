from turtle import *

def draw_equilateral_triangle(thickness, sidelength, pencolor, fillcolor):
    pensize(thickness)
    color(pencolor, fillcolor)
    down()
    begin_fill()
    for i in range(0, 3):
        forward(sidelength)
        left(120)
    end_fill()
    up()
    
def draw_square(thickness, sidelength, pencolor, fillcolor):
    pensize(thickness)
    color(pencolor, fillcolor)
    down()
    begin_fill()
    for i in range(0, 4):
        forward(sidelength)
        left(90)
    end_fill()
    up()
    
def draw_pentagon(thickness, sidelength, pencolor, fillcolor):
    pensize(thickness)
    color(pencolor, fillcolor)
    down()
    begin_fill()
    for i in range(0, 5):
        forward(sidelength)
        left(72)
    end_fill()
    up()

def draw_hexagon(thickness, sidelength, pencolor, fillcolor):
    pensize(thickness)
    color(pencolor, fillcolor)
    down()
    begin_fill()
    for i in range(0, 6):
        forward(sidelength)
        left(60)
    end_fill()
    up()

def draw_octagon(thickness, sidelength, pencolor, fillcolor):
    pensize(thickness)
    color(pencolor, fillcolor)
    down()
    begin_fill()
    for i in range(0, 8):
        forward(sidelength)
        left(45)
    end_fill()
    up()

def draw_star(thickness, sidelength, pencolor, fillcolor):
    pensize(thickness)
    color(pencolor, fillcolor)
    left(35)
    down()
    begin_fill()
    for i in range(0, 5):
        forward(sidelength)
        right(72)
        forward(sidelength)
        left(144)
    end_fill()
    up()

def draw_circle(thickness, radius, pencolor, fillcolor):
    pensize(thickness)
    color(pencolor, fillcolor)
    down()
    begin_fill()
    circle(radius)
    end_fill()
    up()