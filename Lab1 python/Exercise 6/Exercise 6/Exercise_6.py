import turtle
import math

turtle.shape('turtle')

n = 12

for i in range(n):
    t = (2 * math.pi / n) * i
    turtle.goto(100 * math.cos(t), 100 * math.sin(t))
    turtle.stamp()
    turtle.goto(0, 0)