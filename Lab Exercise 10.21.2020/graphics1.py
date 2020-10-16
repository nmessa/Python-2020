## Graphics Demo 1
## Author: nmessa
## Date: 10.1.2014

import pygame, sys

pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255, 255, 255])

dx = 8
dy = 6
posX = 0
posY = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
    pygame.time.delay(20)
    screen.fill([255, 255, 255])
    posX = posX + dx
    posY = posY + dy
    pygame.draw.circle(screen, [0,255,0],[posX,posY], 30, 0)
    pygame.display.flip()
