import turtle

turtle.shape('turtle')

for i in range(1, 11, 1):
    turtle.forward(50 + 10 * i)
    turtle.left(90)
    turtle.forward(50 + 10 * i)
    turtle.left(90)
    turtle.forward(50 + 10 * i)
    turtle.left(90)
    turtle.forward(50 + 10 * i)
    turtle.left(90)
    turtle.penup()
    turtle.goto(-5 * i, -5 * i)
    turtle.pendown()
