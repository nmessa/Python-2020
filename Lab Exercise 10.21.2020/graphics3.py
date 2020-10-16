## Graphics Demo 3
## Author: nmessa
## Date: 10.1.2014

import pygame, sys, random
from pygame.color import THECOLORS

pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255, 255, 255])
line_width = 2

for i in range (100):
    width = random.randint(0, 250)
    height = random.randint(0, 100)
    top = random.randint(0, 400)
    left = random.randint(0, 500)
    color_name = random.choice(list(THECOLORS.keys()))
    color = THECOLORS[color_name]
    pygame.draw.rect(screen, color, [left, top, width, height], line_width)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
