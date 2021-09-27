import turtle
import math

turtle.shape('turtle')

def figure(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for i in range(- 100, 100, 1):
        z = (100 ** 2 - i ** 2) ** 0.5
        turtle.goto(i + 100 + x, z + y)
    for i in range(100, -101, -1):
        z = -(100 ** 2 - i ** 2) ** 0.5
        turtle.goto(i + 100 + x, z + y)

for i in range(6):
    t = (2 * math.pi / 6) * i
    figure(100 * math.cos(t), 100 * math.sin(t))

