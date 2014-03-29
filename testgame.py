__author__ = 'kburke'

import pygame, sys
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()

windowSurface = pygame.display.set_mode((640,480))

font = pygame.font.Font(None, 32)

while True:
    windowSurface.fill(pygame.Color(255,255,255))

    pygame.draw.polygon(windowSurface, pygame.Color(255,0,0),((100,100), (150,150), (200, 100)))

    msgSurface = font.render("Hello world!", False, pygame.Color(0,255,0))
    msgRect = msgSurface.get_rect()
    msgRect.topleft = (300,300)

    windowSurface.blit(msgSurface, msgRect)


    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
        elif event.type == QUIT:
            pygame.quit()
            sys.exit(0)

    pygame.display.update()

    fpsClock.tick(30)