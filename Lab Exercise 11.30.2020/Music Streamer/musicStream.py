##Lab Exercise 11.30.2020 Part II
##Author: 
##musicStream.py
##This program will stream in music from a file

import pygame

pygame.init()
pygame.mixer.init()


def main():
    screen = pygame.display.set_mode((640, 640))
    pygame.display.set_caption("Python Music Streamer")
    
    #create background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 0))
    
    #define fonts
    myFont2 = pygame.font.SysFont("None", 50)
    myFont = pygame.font.SysFont("None", 30)
    
    #create labels for menu
    title = myFont2.render("Streaming Music Player", 1, (0, 0, 255))
    label = myFont.render("Press a choice from the menu", 1, (0, 0, 255))
    label1 = myFont.render("1.  Load Song", 1, (0, 0, 255))
    label2 = myFont.render("2.  Play Song", 1, (0, 0, 255))
    #Add code here

    

    keepGoing = True
    clock = pygame.time.Clock()
    songLoaded = False
    
    while keepGoing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.stop()
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    pygame.mixer.music.load("song3.ogg")
                    songLoaded = True
                elif event.key == pygame.K_2 and songLoaded:
                    pygame.mixer.music.play()
                #Add code here
                    
        #BLIT everything to screen (background, label, title, label1 - 10
        screen.blit(background, (0, 0))
        screen.blit(title, (150, 50))
        screen.blit(label, (100, 540))
        screen.blit(label1, (100, 100))
        screen.blit(label2, (100, 130))
        #Add more labels
        
        pygame.display.flip()     #end of while loop
        
    pygame.display.quit()    #kills display window
    
main()
    
