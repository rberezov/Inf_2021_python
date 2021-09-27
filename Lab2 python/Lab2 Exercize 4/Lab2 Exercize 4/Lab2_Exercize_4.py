import turtle

turtle.shape('turtle')

turtle.forward(400)
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
x = 0
y = 0
Vx = 10
Vy = 50
Ay = -30

for i in range(0, 1000, 1):
    x += Vx * 0.1
    Vy += Ay * 0.1
    y += Vy * 0.1 + Ay * 0.1**2 / 2
    if y < 0:
        y = 0
        Vy = - Vy
    turtle.goto(x, y)

turtle.exitonclick()