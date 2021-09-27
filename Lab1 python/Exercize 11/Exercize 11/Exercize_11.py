import turtle
import math

turtle.shape('turtle')

def figure(t):
    for i in range(- (50 + t * 10), (50 + t * 10), 1):
        z = ((50 + t * 10) ** 2 - i ** 2) ** 0.5
        turtle.goto(i + (50 + t * 10), z)
    for i in range((50 + t * 10), - (50 + t * 10) - 1, -1):
        z = -((50 + t * 10) ** 2 - i ** 2) ** 0.5
        turtle.goto(i + (50 + t * 10), z)
    for i in range(-(50 + t * 10), (50 + t * 10), 1):
        z = ((50 + t * 10) ** 2 - i ** 2) ** 0.5
        turtle.goto(-i - (50 + t * 10), z)
    for i in range((50 + t * 10), -(50 + t * 10) - 1, -1):
        z = -((50 + t * 10) ** 2 - i ** 2) ** 0.5
        turtle.goto(-i - (50 + t * 10), z)


for i in range(6):
    figure(i)
