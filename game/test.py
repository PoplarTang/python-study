import pygame, sys
from math import *
pygame.init()
screen = pygame.display.set_mode((800, 700), 0, 32)
missile = pygame.image.load('element/rect1.png').convert_alpha()

font1 = pygame.font.SysFont('microsoftyaheimicrosoftyaheiui', 23)
textc = font1.render('*', True, (250, 0, 0))
height = missile.get_height()
width = missile.get_width()


clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    clock.tick(300)

    screen.fill((0, 88, 0))
    screen.blit(missile, (0, 0))
    screen.blit(textc, (10, 10))  # 鼠标用一个红色*代替
    pygame.display.update()
