from shapes import *
from random import randrange

if __name__ == "__main__":
  # prepare screen
  Screen().bgcolor("#0F1033")
  hideturtle()
  speed('fastest')
  up()
  
  # draw stars in night sky
  for i in range(0, 50):
    goto(randrange(-200, 200), randrange(-200, 200))
    draw_shape("star", 1, randrange(10), True, "gold", "gold")