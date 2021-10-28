import linecache
import json
import time
from math import sqrt
from random import randint
import pygame
from pygame.constants import *
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
    """
    def __init__(self):
        self.number_of_clicks_to_delete = randint(1, 5)
        self.lives = 150
        self.x_coordinate = 100
        self.y_coordinate = 800
        self.radius = 20
        self.color = COLORS[randint(0, 5)]
        self.velocityx = 0
        self.velocityy = 0
        self.Birth = 0

    def moving(self, t):
        """
        Moving the ball
        """
        self.velocityy = self.velocityy + 0.005 * (t - self.Birth)
        self.x_coordinate = self.x_coordinate + self.velocityx 
        self.y_coordinate = self.y_coordinate + self.velocityy
        if self.x_coordinate > 1200 - self.radius or self.x_coordinate - self.radius < 0:
            self.velocityx = -self.velocityx
        if self.y_coordinate > 900 - self.radius or self.y_coordinate  - self.radius < 0:
            self.velocityy = -self.velocityy
            if self.y_coordinate > 900 - self.radius:
                self.y_coordinate = 900  - self.radius

    def draw(self):
        """
        A ball is being drawn
        """
        pygame.draw.circle(screen, self.color, (self.x_coordinate, self.y_coordinate), self.radius)

    def delete(self):
        """
        The ball is painted black before being removed
        """
        self.color = BLACK

class gun:
    def __init__(self):
        self.x = 0
        self.y = 0

    def draw(self, t):
        if (self.x - 100) ** 2 + (self.y - 800) ** 2 != 0:
            pygame.draw.line(screen,YELLOW ,(100 - (self.x - 100) * t / sqrt((self.x - 100) ** 2 \
                + (self.y - 800) ** 2), 800 + (800 - self.y) * t / sqrt((self.x - 100) ** 2 \
                + (self.y - 800) ** 2)), (100, 800), 20)

class aim:
    def __init__(self):
        self.object_ball = Ball()
        self.object_ball.x_coordinate = randint(400, 1000)
        self.object_ball.y_coordinate = randint(100, 700)
        self.object_ball.radius = 20

    def draw(self):
        self.object_ball.draw()

def number(num, posx_0, posy_0, size):
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
        posx = posx_0 - 120 * size / 50 * k
        tempx = posx
        tempy = posy_0
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
                    tempx = tempx + size / 50 * x_coordinate
                    tempy = tempy - size / 50 * y_coordinate
                else:
                    pygame.draw.line(screen, (255, 255, 255), (tempx, tempy),
                        (posx + size / 50 * x_coordinate, posy_0 - size / 50 * y_coordinate),
                       size * 10 // 50)
                    tempx = posx + size * x_coordinate // 50
                    tempy = posy_0 - size / 50 * y_coordinate
pygame.display.update()
clock = pygame.time.Clock()

data = {}
with open ('input.json', 'rt') as f:
    data = json.load(f)

FINISHED = False
NICKNAME = ''
NUMBER_OF_SYMBOL = 0
NUMBER_OF_ENTER = 0
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
                if NUMBER_OF_ENTER == 0:
                    if data.get(NICKNAME) is None:
                        data[NICKNAME] = 0
                    text3 = f2.render('Your record:' + str(data[NICKNAME]),
                                     True, (180, 0, 0))
                    screen.blit(text3, (400, 500))
                    NUMBER_OF_ENTER = NUMBER_OF_ENTER + 1
                else:
                    NUMBER_OF_ENTER = NUMBER_OF_ENTER + 1
                    FINISHED = True
            elif pygame.key.name(event.key) == 'space':
                NUMBER_OF_SYMBOL = NUMBER_OF_SYMBOL + 1
                NICKNAME = NICKNAME + ' '
            elif pygame.key.name(event.key) == 'left shift' \
               or pygame.key.name(event.key) == 'right shift':
                NICKNAME = NICKNAME + ''
            elif pygame.key.name(event.key) == 'backspace':
                if NUMBER_OF_SYMBOL != 0 and NUMBER_OF_ENTER == 0:
                    NICKNAME = NICKNAME[:-1]
                    NUMBER_OF_SYMBOL = NUMBER_OF_SYMBOL - 1
                    pygame.draw.rect(screen, (0, 0, 0),
                                    (430 + NUMBER_OF_SYMBOL * 30, 450, 50, 50))
            else:
                keyname = pygame.key.name(event.key)
                NICKNAME = NICKNAME + keyname
                f1 = pygame.font.Font(None, 50)
                NUMBER_OF_SYMBOL = NUMBER_OF_SYMBOL + 1
                text1 = f1.render(keyname, True, (180, 0, 0))
                screen.blit(text1, (400 + NUMBER_OF_SYMBOL * 30, 450))
if NUMBER_OF_ENTER == 2: #Checks whether the player has exited
    FINISHED = False

LIST_OF_BALLS = []
SCORE = 0
NUMBER_OF_EXECUTIONS_MAIN_CYCLES = 0
Time_of_pressing_the_key = 0
Number_of_cycles_before_releasing_the_key = 0
The_number_of_shots_before_hitting = 0
sh = gun()
ai = aim()
while not FINISHED: #The main cycle of the game
    clock.tick(FPS)
    ai.draw()
    NUMBER_OF_EXECUTIONS_MAIN_CYCLES = NUMBER_OF_EXECUTIONS_MAIN_CYCLES + 1
    if Number_of_cycles_before_releasing_the_key < 100:
        Number_of_cycles_before_releasing_the_key = Number_of_cycles_before_releasing_the_key + 1
    for i in range(len(LIST_OF_BALLS)):
        LIST_OF_BALLS[i].moving(NUMBER_OF_EXECUTIONS_MAIN_CYCLES)
        LIST_OF_BALLS[i].draw()
    number(SCORE, LENGHT - 100, 150, 50)
    if Time_of_pressing_the_key != 0:
        sh.draw(25 + Number_of_cycles_before_releasing_the_key)
    else:
        sh.draw(25)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            Time_of_pressing_the_key = 0.04
            Number_of_cycles_before_releasing_the_key = 0
            The_number_of_shots_before_hitting = The_number_of_shots_before_hitting + 1
        elif event.type == pygame.MOUSEMOTION:
            sh.x = event.pos[0]
            sh.y = event.pos[1]
        elif event.type == pygame.KEYDOWN:
            if pygame.key.name(event.key) == 'escape':
                FINISHED = True
        elif event.type == pygame.QUIT:
            FINISHED = True
        elif event.type == pygame.MOUSEBUTTONUP:
            x = Ball()
            x.Birth = NUMBER_OF_EXECUTIONS_MAIN_CYCLES
            x.velocityx = (event.pos[0] - 100) / sqrt((event.pos[0] + 100) ** 2 + (event.pos[1] - 800) ** 2)\
               * Time_of_pressing_the_key * Number_of_cycles_before_releasing_the_key * 5
            x.velocityy = (event.pos[1] - 800) / sqrt((event.pos[0] + 100) ** 2 + (event.pos[1] - 800) ** 2)\
               * Time_of_pressing_the_key * Number_of_cycles_before_releasing_the_key * 5
            LIST_OF_BALLS.append(x)
            Time_of_pressing_the_key = 0

    for i in reversed(range(len(LIST_OF_BALLS))):
        if LIST_OF_BALLS[i].lives - 1 >= 0:
            LIST_OF_BALLS[i].lives = LIST_OF_BALLS[i].lives - 1
        else:
            LIST_OF_BALLS[i].delete()
            LIST_OF_BALLS.pop(i)

    for i in reversed(range(len(LIST_OF_BALLS))):
        if (LIST_OF_BALLS[i].x_coordinate - ai.object_ball.x_coordinate) ** 2 \
            + (LIST_OF_BALLS[i].y_coordinate - ai.object_ball.y_coordinate) ** 2 \
            < (ai.object_ball.radius + LIST_OF_BALLS[i].radius) ** 2:
            screen.fill(BLACK)
            temp = time.time()
            while time.time() - temp < 1: {}
            SCORE = SCORE + 1
            f4 = pygame.font.Font(None, 50)
            text4 = f4.render('You took ' + str(The_number_of_shots_before_hitting) +' shots to hit!'\
            , True, (180, 0, 0))
            temp = time.time()
            while (time.time() - temp < 2):
                screen.blit(text4, (350 , 400))
                pygame.display.update()
            The_number_of_shots_before_hitting = 0
            ai = aim()
            LIST_OF_BALLS = []

    screen.fill(BLACK)

if SCORE > data[NICKNAME]: #Congratulations to the player if he make the record
    screen.fill(BLACK)
    data[NICKNAME] = SCORE
    with open ('input.json', 'wt') as f:
        json.dump(data, f)
    FINISHED = False
    while not FINISHED:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                FINISHED = True
            elif event.type == pygame.KEYDOWN:
                if pygame.key.name(event.key) == 'escape':
                    FINISHED = True
        f4 = pygame.font.Font(None, 50)
        text4 = f4.render('Congratulations! You have a new record:'\
           + ' ' + str(SCORE), True, (180, 0, 0))
        screen.blit(text4, (350 , 400))
        pygame.display.update()
pygame.quit()
