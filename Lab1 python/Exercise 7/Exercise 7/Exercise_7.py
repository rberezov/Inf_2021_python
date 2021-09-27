import turtle
import math

turtle.shape('turtle')

a = 10

for i in range(0, 100000, 1):
    turtle.goto(i / 10 * math.cos(i / 100) - 1, i / 10 * math.sin(i / 100))
