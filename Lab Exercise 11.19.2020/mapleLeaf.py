## mapleLeafBounce.py
## Author: nmessa
## This program takes a maple leaf drawn with the lines function and animates it.
## When collision with wall is detected, the maple leaf "bounces"


import pygame, sys

pygame.init()
dots = [[221, 432], [225, 331], [133, 342], [141, 310],
[51, 230], [74, 217], [58, 153], [114, 164],
[123, 135], [176, 190], [159, 77], [193, 93],
[230, 28], [267, 93], [301, 77], [284, 190],
[327, 135], [336, 164], [402, 153], [386, 217],
[409, 230], [319, 310], [327, 342], [233, 331],
[237, 432]]

#set granularity of animation
dx = 1
dy = 1

#setup screen to paint on
screen = pygame.display.set_mode([1300,850])
screen.fill([255, 255, 255])

#draw maple leaf
pygame.draw.lines(screen, [255,0,0],True, dots, 2)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
    #check for collision with wall
    for i in range(len(dots)):
        if dots[i][0] > screen.get_width() or dots[i][0] < 0:
            dx = - dx    # bounce in the X direction
            break
        if dots[i][1] > screen.get_height() or dots[i][1] < 0:
            dy = - dy    # bounce in the Y direction
            break
            
    #update points
    for i in range(len(dots)):
        dots[i][0] += dx
        dots[i][1] += dy

    #redraw the maple leaf in new position determined by updated dots list
    screen.fill([255, 255, 255])
    pygame.draw.lines(screen, [255,0,0],True, dots, 2)
    pygame.display.flip()
    
