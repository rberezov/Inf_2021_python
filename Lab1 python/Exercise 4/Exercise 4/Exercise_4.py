import turtle

turtle.shape('turtle')

y = 0

for i in range(- 100, 100, 1):
    y = (100 ** 2 - i ** 2) ** 0.5
    turtle.goto(i + 100, y)

for i in range(100, -100, -1):
    y = -(100 ** 2 - i ** 2) ** 0.5
    turtle.goto(i + 100, y)
