import turtle
from random import *

turtle.shape('turtle')



for i in range(10000):
    teta = randint(0, 360)
    r = randint(5, 80)
    turtle.left(teta)
    turtle.forward(r)