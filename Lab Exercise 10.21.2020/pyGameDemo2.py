## Pygame demo
## Author: nmessa
## Date: 10.1.2017
## This program displays a filled circle that cycles through all colors

import pygame, sys

pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255, 255, 255])

posX = 320
posY = 240

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()

    screen.fill([255, 255, 255])
    for r in range(0,256, 10):
        for g in range(0,256,10):
            for b in range(0,256,10):
                pygame.draw.circle(screen, [r,g,b],[posX,posY], 100, 0)
                pygame.display.flip()
