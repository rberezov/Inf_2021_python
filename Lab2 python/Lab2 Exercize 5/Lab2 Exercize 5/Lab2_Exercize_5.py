from random import randint
import turtle

turtle.penup()
turtle.goto(-200, -200)
turtle.pendown()
turtle.forward(400)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(400)
turtle.penup()


number_of_turtles = 5
steps_of_time_number = 1000


pool = [turtle.Turtle(shape='turtle') for i in range(number_of_turtles)]

for unit in pool:
    unit.penup()
    unit.x = randint(-200, 200)
    unit.y = randint(-200, 200)
    unit.Vx = randint(-10, 10)
    unit.Vy = randint(-10, 10)
    


for i in range(steps_of_time_number):
    for unit in pool:
        unit.x += unit.Vx * i * 0.005
        unit.y += unit.Vy * i * 0.005
        unit.goto(unit.x, unit.y)
        if unit.x <= -200:
            unit.x = -200
            unit.Vx = - unit.Vx
        if unit.y <= -200:
            unit.y = - 200
            unit.Vy = - unit.Vy
        if unit.x >= 200:
            unit.x = 200
            unit.Vx = - unit.Vx
        if unit.y >= 200:
            unit.y = 200
            unit.Vy = - unit.Vy

