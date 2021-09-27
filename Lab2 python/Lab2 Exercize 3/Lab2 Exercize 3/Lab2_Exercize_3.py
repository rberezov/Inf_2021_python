import turtle
import linecache

turtle.shape('turtle')

def number(A, x_0):

    C = linecache.getline('num.txt', A + 1)
    
    turtle.penup()
    for i in range(len(C)):
        if C[i] == '(':
            i = i + 1
            x = 0
            y = 0

            while C[i] != ',':
                x = x * 10 + ord(C[i]) - ord('0')
                i = i + 1

            i = i + 1;
            while C[i] != ')':
                y = y * 10 + ord(C[i]) - ord('0')
                i = i + 1
            
            turtle.goto(x + x_0, y)
            turtle.pendown()

    turtle.penup()








A = list(map(int, input().split()))
for i in range(len(A)):
    number(A[i], i * 110)

turtle.exitonclick()
