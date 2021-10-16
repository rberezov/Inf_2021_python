import linecache
import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 90
length = 1200
width = 900
screen = pygame.display.set_mode((length, width))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

class Ball:
    def __init__(self):
        self.x = randint(200, 1000)
        self.y = randint(200, 800)
        self.r = randint(30, 99)
        self.color = COLORS[randint(0, 5)]
        self.v = (randint(-12, 12), randint(-12, 12))

    def moving(self):
        self.x = self.x + self.v[0]
        self.y = self.y + self.v[1]
        if self.x > 1200 - self.r or self.x - self.r < 0:
            vx, vy = self.v
            self.v = -vx, vy
        if self.y > 900  - self.r or self.y  - self.r < 0:
            vx, vy = self.v
            self.v = vx, -vy

    def draw(self):
        circle(screen, self.color, (self.x, self.y), self.r)

    def delete(self):
        self.color = BLACK

def number(num):

    A = []
    if num == 0:
        A.append(0)
    while num != 0:
        A.append(num % 10)
        num = num // 10

    for k in reversed(range(len(A))):
        C = linecache.getline('num.txt', A[k] + 1)
        posx = length - 100 - 120 * k
        posy = 150
        tempx = posx
        tempy = posy
        Numbe_of_numbers_read = 0
        for i in range(len(C)):
            if C[i] == '(':
                i = i + 1
                x = 0
                y = 0
                while C[i] != ',':
                    x = x * 10 + ord(C[i]) - ord('0')
                    i = i + 1
                Numbe_of_numbers_read = Numbe_of_numbers_read + 1
 
                i = i + 1;
                while C[i] != ')':
                    y = y * 10 + ord(C[i]) - ord('0')
                    i = i + 1
                Numbe_of_numbers_read = Numbe_of_numbers_read + 1

                if Numbe_of_numbers_read == 2:
                    tempx = tempx + x
                    tempy = tempy - y
                else:
                    line(screen, (255, 255, 255), (tempx, tempy), (posx + x, posy - y), 10)
                    tempx = posx + x
                    tempy = posy - y


            




pygame.display.update()
clock = pygame.time.Clock()
finished = False

list_of_balls = []
score = 0
number_of_while = 0

while not finished:
    number_of_while = number_of_while + 1;

    clock.tick(FPS)

    if number_of_while % 30 == 0 or number_of_while == 0:
        list_of_balls.append(Ball())
    

    for i in range(len(list_of_balls)):
        list_of_balls[i].moving()
        list_of_balls[i].draw()

    number(score)

    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in reversed(range(len(list_of_balls))):
                if (event.pos[0] - list_of_balls[i].x) ** 2 + (event.pos[1] - list_of_balls[i].y) ** 2 < list_of_balls[i].r ** 2:
                    list_of_balls[i].delete()
                    list_of_balls.pop(i)
                    score = score + 1
    screen.fill(BLACK)
            

pygame.quit()
