import turtle

turtle.shape('turtle')

def figure(x, y, r):
    turtle.penup()
    turtle.goto(x - r, y)
    turtle.pendown()
    for i in range(- r, r, 1):
        z = (r ** 2 - i ** 2) ** 0.5
        turtle.goto(i + x, z + y)
    for i in range(r, - r - 1, -1):
        z = -(r ** 2 - i ** 2) ** 0.5
        turtle.goto(i + x, z + y)

def figure1(x, y, r):
    turtle.penup()
    turtle.goto(x + r, y)
    turtle.pendown()
    for i in range(r, - r - 1, -1):
        z = -(r ** 2 - i ** 2) ** 0.5
        turtle.goto(i + x, z + y)

turtle.begin_fill()	
turtle.color("yellow")
figure(0, 0, 100)
turtle.end_fill()

turtle.begin_fill()	
turtle.color("blue")
figure(-30, 60 , 10)
turtle.end_fill()

turtle.begin_fill()	
turtle.color("blue")
figure(30, 60, 10)
turtle.end_fill()

turtle.penup()
turtle.goto(0, 30)
turtle.pendown()
turtle.color("black")
turtle.width(5)
turtle.goto(0, 0)

turtle.color("red")
figure1(0, 0, 60)