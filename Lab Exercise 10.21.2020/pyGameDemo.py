##### PyGame example ########
## Author: nmessa
## Date: 10.1.2017
## This program displays all pygame events
import sys

#import and initpygame
import pygame
pygame.init()

#create the screen
window = pygame.display.set_mode((640, 480)) 

#draw a line
pygame.draw.line(window, (255, 255, 255), (0, 0), (30, 50))
#draw it to the screen
pygame.display.flip()

#input handling (boilerplate code):
while True: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit(0) 
        else: 
            print (event)
