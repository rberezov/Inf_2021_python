import turtle

turtle.shape('turtle')

n = 11

for i in range(n):
    turtle.forward(100)
    turtle.left(180 - 180 / n)
