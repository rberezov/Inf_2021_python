import turtle
import math

turtle.shape('turtle')

def figure(n):
    r = 20 * n
    turtle.penup()
    turtle.goto(r, 0)
    turtle.pendown()
    for i in range(n + 1):
        t = (2 * math.pi / n) * i
        turtle.goto(r * math.cos(t), r * math.sin(t))

for i in range(3, 12, 1):
    figure(i)
