from shapes import *

if __name__ == "__main__":
    shape("turtle")
    up()
    goto(-75, 75)
    draw_shape("triangle", 2, 50, False)
    goto(0, 75)
    draw_shape("square", 2, 45, True, "red", "orange")
    goto(85, 75)
    draw_shape("pentagon", 2, 30, True, "blue", "green")
    goto(-70, 0)
    draw_shape("hexagon",2, 30, False)
    goto(10, 0)
    draw_shape("octagon", 2, 21, True, "black", "purple")
    goto(80, 0)
    draw_shape("star", 2, 25, True, "orange", "gold")
    goto(33, -75)
    draw_shape("circle", 2, 28, False, "red", "red")
