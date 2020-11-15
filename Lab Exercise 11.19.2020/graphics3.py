##Lab Exercise 11.19.2020 Problem 3
##Author: nmessa
##File: graphics3.py

import pygame, sys
import math

pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255, 255, 255])
plotPoints = []

for x in range(0, 640):
    y = int(math.sin(x/640.0 * 4 * math.pi) * 200 + 240)
    plotPoints.append([x, y])

pygame.draw.lines(screen, [0,0,0],False, plotPoints, 1)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
