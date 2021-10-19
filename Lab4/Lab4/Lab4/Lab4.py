import linecache
import json
import pygame
from math import sqrt
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
        self.max_r = 99
        self.number_of_clicks_to_delete = randint(1, 5)
        self.lives = randint(500, 1000)
        self.x = randint(200, 1000)
        self.y = randint(200, 800)
        self.r = randint(30, self.max_r)
        self.color = COLORS[randint(0, 5)]
        self.v = (randint(-6, 6), randint(-6, 6))

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

data = {}
with open ('input.json') as f:
    data = json.load(f)

finished = False
nickname = ''
number_of_symbol = 0
number_of_enter = 0
while not finished:
    f2 = pygame.font.Font(None, 50)
    text2 = f2.render('Plese, enter your nickname:', True, (180, 0, 0))
    screen.blit(text2, (400 , 400))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN:
            if pygame.key.name(event.key) == 'escape':
                finished = True
            elif pygame.key.name(event.key) == 'return':
                if number_of_enter == 0:
                    if data.get(nickname) == None:
                       data[nickname] = 0
                    text3 = f2.render('Your record:' + str(data[nickname]), True, (180, 0, 0))
                    screen.blit(text3, (400, 500))
                    number_of_enter = number_of_enter + 1
                else:
                    number_of_enter = number_of_enter + 1
                    finished = True
            elif pygame.key.name(event.key) == 'space':
                number_of_symbol = number_of_symbol + 1
                nickname = nickname + ' '
            elif pygame.key.name(event.key) == 'left shift' or pygame.key.name(event.key) == 'right shift':
                nickname = nickname + ''
            elif pygame.key.name(event.key) == 'backspace':
                if number_of_symbol != 0 and number_of_enter == 0:
                    nickname = nickname[:-1]
                    number_of_symbol = number_of_symbol - 1
                    rect(screen, (0, 0, 0), (430 + number_of_symbol * 30, 450, 50, 50))
            else:
                keyname = pygame.key.name(event.key)
                nickname = nickname + keyname
                f1 = pygame.font.Font(None, 50)
                number_of_symbol = number_of_symbol + 1
                text1 = f1.render(keyname, True, (180, 0, 0))
                screen.blit(text1, (400 + number_of_symbol * 30, 450))



if number_of_enter == 2:
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
        elif event.type == pygame.KEYDOWN:
            if pygame.key.name(event.key) == 'escape':
                finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            the_number_of_balls_hit = 0;
            for i in reversed(range(len(list_of_balls))):
                if (event.pos[0] - list_of_balls[i].x) ** 2 + (event.pos[1] - list_of_balls[i].y) ** 2 < list_of_balls[i].r ** 2:
                    the_number_of_balls_hit = the_number_of_balls_hit + 1
                    if list_of_balls[i].number_of_clicks_to_delete - 1 > 0:
                        list_of_balls[i].number_of_clicks_to_delete = list_of_balls[i].number_of_clicks_to_delete - 1
                    else:
                        list_of_balls[i].delete()
                        score = score + list_of_balls[i].max_r // list_of_balls[i].r + round(sqrt(list_of_balls[i].v[1] ** 2 + list_of_balls[i].v[1] ** 2)) // 3 + list_of_balls[i].number_of_clicks_to_delete // 2
                        list_of_balls.pop(i)
            if the_number_of_balls_hit == 0 and score != 0:
                score = score - 1


    for i in reversed(range(len(list_of_balls))):
        if list_of_balls[i].lives - 1 >= 0:
            list_of_balls[i].lives = list_of_balls[i].lives - 1
        else:
            list_of_balls[i].delete()
            list_of_balls.pop(i)

    screen.fill(BLACK)

if score > data[nickname]:
    screen.fill(BLACK)
    data[nickname] = score
    with open ('input.json', 'w') as f:
        json.dump(data, f)
    finished = False
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.KEYDOWN:
                if pygame.key.name(event.key) == 'escape':
                    finished = True
        f4 = pygame.font.Font(None, 50)
        text4 = f4.render('Congratulations! You have a new record:' + ' ' +str(score), True, (180, 0, 0))
        screen.blit(text4, (350 , 400))
        pygame.display.update()
        
     

            

pygame.quit()
