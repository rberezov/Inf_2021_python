import linecache
import json
from math import sqrt
from random import randint
import pygame
from pygame.draw import *
pygame.init()

FPS = 90
LENGHT = 1200
WIDTH = 900
screen = pygame.display.set_mode((LENGHT, WIDTH))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

class Ball:
    """ A ball is being created
    number_of_clicks_to_delete - Number of taps to remove the ball
    lives - Number of lives
    x, y, r  - Coordinates of the center of the ball and radius
    v - Speed
    """
    max_radius = 99
    min_radius = 30
    def __init__(self):
        self.number_of_clicks_to_delete = randint(1, 5)
        self.lives = randint(500, 1000)
        self.x_coordinate = randint(200, 1000)
        self.y_coordinate = randint(200, 800)
        self.radius = randint(self.min_radius, self.max_radius)
        self.color = COLORS[randint(0, 5)]
        self.velocity = (randint(-6, 6), randint(-6, 6))

    def moving(self):
        """
        Moving the ball
        """
        self.x_coordinate = self.x_coordinate + self.velocity[0]
        self.y_coordinate = self.y_coordinate + self.velocity[1]
        if self.x_coordinate > 1200 - self.radius or self.x_coordinate - self.radius < 0:
            velocityx, velocityy = self.velocity
            self.velocity = -velocityx, velocityy
        if self.y_coordinate > 900  - self.radius or self.y_coordinate  - self.radius < 0:
            velocityx, velocityy = self.velocity
            self.velocity = velocityx, -velocityy

    def draw(self):
        """
        A ball is being drawn
        """
        circle(screen, self.color, (self.x_coordinate, self.y_coordinate), self.radius)

    def delete(self):
        """
        The ball is painted black before being removed
        """
        self.color = BLACK

def number(num):
    """
    Displays the score in the game on the screen
    """
    numbers = []
    if num == 0:
        numbers.append(0)
    while num != 0:
        numbers.append(num % 10)
        num = num // 10

    for k in reversed(range(len(numbers))):
        font_information = linecache.getline('num.txt', numbers[k] + 1)
        posx = LENGHT - 100 - 120 * k
        posy = 150
        tempx = posx
        tempy = posy
        numbe_of_numbers_read = 0

        for j in range(len(font_information)):
            if font_information[j] == '(':
                j = j + 1
                x_coordinate = 0
                y_coordinate = 0
                while font_information[j] != ',':
                    x_coordinate = x_coordinate * 10 + ord(font_information[j]) - ord('0')
                    j = j + 1
                numbe_of_numbers_read = numbe_of_numbers_read + 1
                j = j + 1
                while font_information[j] != ')':
                    y_coordinate = y_coordinate * 10 + ord(font_information[j]) - ord('0')
                    j = j + 1
                numbe_of_numbers_read = numbe_of_numbers_read + 1
                if numbe_of_numbers_read == 2:
                    tempx = tempx + x_coordinate
                    tempy = tempy - y_coordinate
                else:
                    line(screen, (255, 255, 255), (tempx, tempy),
                        (posx + x_coordinate, posy - y_coordinate), 10)
                    tempx = posx + x_coordinate
                    tempy = posy - y_coordinate
pygame.display.update()
clock = pygame.time.Clock()

data = {}
with open ('input.json', 'rt') as f:
    data = json.load(f)

FINISHED = False
NICKNAME = ''
number_of_symbol = 0
number_of_enter = 0
while not FINISHED: #Entering the user name
    f2 = pygame.font.Font(None, 50)
    text2 = f2.render('Plese, enter your nickname:', True, (180, 0, 0))
    screen.blit(text2, (400 , 400))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            FINISHED = True
        elif event.type == pygame.KEYDOWN:
            if pygame.key.name(event.key) == 'escape':
                FINISHED = True
            elif pygame.key.name(event.key) == 'return':
                if number_of_enter == 0:
                    if data.get(NICKNAME) is None:
                        data[NICKNAME] = 0
                    text3 = f2.render('Your record:' + str(data[NICKNAME]),
                                     True, (180, 0, 0))
                    screen.blit(text3, (400, 500))
                    number_of_enter = number_of_enter + 1
                else:
                    number_of_enter = number_of_enter + 1
                    FINISHED = True
            elif pygame.key.name(event.key) == 'space':
                number_of_symbol = number_of_symbol + 1
                NICKNAME = NICKNAME + ' '
            elif pygame.key.name(event.key) == 'left shift' \
               or pygame.key.name(event.key) == 'right shift':
                NICKNAME = NICKNAME + ''
            elif pygame.key.name(event.key) == 'backspace':
                if number_of_symbol != 0 and number_of_enter == 0:
                    NICKNAME = NICKNAME[:-1]
                    number_of_symbol = number_of_symbol - 1
                    rect(screen, (0, 0, 0), (430 + number_of_symbol * 30, 450, 50, 50))
            else:
                keyname = pygame.key.name(event.key)
                NICKNAME = NICKNAME + keyname
                f1 = pygame.font.Font(None, 50)
                number_of_symbol = number_of_symbol + 1
                text1 = f1.render(keyname, True, (180, 0, 0))
                screen.blit(text1, (400 + number_of_symbol * 30, 450))
if number_of_enter == 2:
    FINISHED = False

list_of_balls = []
score = 0
number_of_while = 0

while not FINISHED: #The main cycle of the game
    clock.tick(FPS)
    number_of_while = number_of_while + 1

    if number_of_while % 30 == 0 or number_of_while == 0:
        list_of_balls.append(Ball())
    for i in range(len(list_of_balls)):
        list_of_balls[i].moving()
        list_of_balls[i].draw()

    number(score)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            FINISHED = True
        elif event.type == pygame.KEYDOWN:
            if pygame.key.name(event.key) == 'escape':
                FINISHED = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            the_number_of_balls_hit = 0
            for i in reversed(range(len(list_of_balls))):
                if (event.pos[0] - list_of_balls[i].x_coordinate) ** 2 \
                    + (event.pos[1] - list_of_balls[i].y_coordinate) ** 2 \
                    < list_of_balls[i].radius ** 2:
                    the_number_of_balls_hit = the_number_of_balls_hit + 1
                    if list_of_balls[i].number_of_clicks_to_delete - 1 > 0:
                        list_of_balls[i].number_of_clicks_to_delete = \
                            list_of_balls[i].number_of_clicks_to_delete - 1
                    else:
                        list_of_balls[i].delete()
                        score = score + list_of_balls[i].max_radius \
                            // list_of_balls[i].radius \
                            + round(sqrt(list_of_balls[i].velocity[1] ** 2 \
                           + list_of_balls[i].velocity[1] ** 2)) // 3 \
                           + list_of_balls[i].number_of_clicks_to_delete // 2
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

if score > data[NICKNAME]: #Congratulations to the player if he make the record
    screen.fill(BLACK)
    data[NICKNAME] = score
    with open ('input.json', 'wt') as f:
        json.dump(data, f)
    finished = False
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.KEYDOWN:
                if pygame.key.name(event.key) == 'escape':
                    FINISHED = True
        f4 = pygame.font.Font(None, 50)
        text4 = f4.render('Congratulations! You have a new record:' + ' ' +str(score),
                         True, (180, 0, 0))
        screen.blit(text4, (350 , 400))
        pygame.display.update()
pygame.quit()
