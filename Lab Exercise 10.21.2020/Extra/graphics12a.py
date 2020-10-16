#Author: nmessa
#Date: 10.4.2017
#Animates a drawn graphic instead of a bitmapped graphic object
import pygame, sys

pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255, 255, 255])
#my_ball = pygame.image.load('beach_ball.png')
x = 50
y = 50
x_speed = 10
y_speed = 10
radius = 30
#pygame.draw.circle(screen, [255,0,0],[x, y], radius, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()

    pygame.time.delay(20)
    pygame.draw.rect(screen, [255,255,255], [x-radius, y-radius, radius, radius], 0)
    x = x + x_speed
    y = y + y_speed

    if x > screen.get_width() - radius or x - radius < 0:
        x_speed = - x_speed
    if y > screen.get_height() - radius or y - radius < 0:
        y_speed = -y_speed
        
    screen.fill([255, 255, 255])
    #pygame.draw.circle(screen, [0,255,0],[x-20, y-20], 20, 0)
    pygame.draw.circle(screen, [255,0,0],[x, y], radius, 0)
    
    pygame.display.flip()
