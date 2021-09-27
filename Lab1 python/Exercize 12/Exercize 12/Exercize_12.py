import turtle
import math

turtle.shape('turtle')

def figure(x, y):
    for i in range(- 100, 100, 1):
        z = (100 ** 2 - i ** 2) ** 0.5
        turtle.goto(i + 100 + x - x / 5, z + y)
    for i in range(20, -20, -1):
        z = -(20 ** 2 - i ** 2) ** 0.5
        turtle.goto(i + 180 - x / 5 + x, z + y)

for i in range(6):
    figure(i * 200, i)