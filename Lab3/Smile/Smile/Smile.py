import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((128, 128, 128))

circle(screen, (255, 255, 0), (200, 200), 150)        #голова
circle(screen, (255, 0, 0), (150, 150), 30)           #левый глаз
circle(screen, (0, 0, 0), (150, 150), 10)
circle(screen, (255, 0, 0), (250, 150), 50)           #правый глаз
circle(screen, (0, 0, 0), (250, 150), 10)
rect(screen, (0, 0, 0), ((100, 250), (200, 25)))      #рот
polygon(screen, (0, 0, 0), [(80, 75), (180, 125),     #брови
                               (175, 135), (75, 85)])
polygon(screen, (0, 0, 0), [(320, 75), (220, 125),
                               (225, 135), (325, 85)])


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
