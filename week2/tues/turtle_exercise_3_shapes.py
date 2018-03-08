from turtle import *

def draw_equilateral_triangle(thickness, sidelength, fill=False, pen_color='black', fill_color=None):
    pensize(thickness)
    down()
    pencolor(pen_color)
    if fill:
        fillcolor(fill_color)
        begin_fill()
    for i in range(0, 3):
        forward(sidelength)
        left(120)
    end_fill()
    up()
    
def draw_square(thickness, sidelength, fill=False, pen_color='black', fill_color=None):
    pensize(thickness)
    down()
    pencolor(pen_color)
    if fill:
        fillcolor(fill_color)
        begin_fill()
    for i in range(0, 4):
        forward(sidelength)
        left(90)
    end_fill()
    up()
    
def draw_pentagon(thickness, sidelength, fill=False, pen_color='black', fill_color=None):
    pensize(thickness)
    down()
    pencolor(pen_color)
    if fill:
        fillcolor(fill_color)
        begin_fill()
    for i in range(0, 5):
        forward(sidelength)
        left(72)
    end_fill()
    up()

def draw_hexagon(thickness, sidelength, fill=False, pen_color='black', fill_color=None):
    pensize(thickness)
    down()
    pencolor(pen_color)
    if fill:
        fillcolor(fill_color)
        begin_fill()
    for i in range(0, 6):
        forward(sidelength)
        left(60)
    end_fill()
    up()

def draw_octagon(thickness, sidelength, fill=False, pen_color='black', fill_color=None):
    pensize(thickness)
    down()
    pencolor(pen_color)
    if fill:
        fillcolor(fill_color)
        begin_fill()
    for i in range(0, 8):
        forward(sidelength)
        left(45)
    end_fill()
    up()

def draw_star(thickness, sidelength, fill=False, pen_color='black', fill_color=None):
    pensize(thickness)
    down()
    pencolor(pen_color)
    if fill:
        fillcolor(fill_color)
        begin_fill()
    left(35)
    for i in range(0, 5):
        forward(sidelength)
        right(72)
        forward(sidelength)
        left(144)
    end_fill()
    up()

def draw_circle(thickness, radius, fill=False, pen_color='black', fill_color=None):
    pensize(thickness)
    down()
    pencolor(pen_color)
    if fill:
        fillcolor(fill_color)
        begin_fill()
    circle(radius)
    end_fill()
    up()