"""
Name: 
Lab Exercise 11/30/2020
pyTunes_starter.py
"""

import pygame
pygame.init()
pygame.mixer.init()

def main():
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("PyTunes")
    
    #create background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 0))
    
    #create labels for menu
    myFont = pygame.font.SysFont("None", 30)
    label = myFont.render("Press a number to hear a song", 1, (0, 0, 255))
    label1 = myFont.render("1.    Song Name", 1, (0, 0, 255))
    label2 = myFont.render("2.    Another Song Name", 1, (0, 0, 255))
    labelQuit = myFont.render("Press ESC key to quit", 1, (0, 0, 255))
    
    #ADD LABELS FOR MORE SONGS

    
    #create songs
    mySong1 = pygame.mixer.Sound("song1.ogg")
    mySong2 = pygame.mixer.Sound("song2.ogg")
    
    #ADD MORE SONGS HERE

    keepGoing = True
    clock = pygame.time.Clock()
    
    while keepGoing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    pygame.mixer.stop()      #kill any other songs playing
                    mySong1.play()               #play song 1
                elif event.key == pygame.K_2:
                    pygame.mixer.stop()
                    mySong2.play()
                    
                #ADD MORE ELIF FOR MORE SONG CHOICES
                    
                elif event.key == pygame.K_ESCAPE:
                    keepGoing = False
                    pygame.mixer.stop()     #kills the music
    
        screen.blit(background, (0, 0))
        screen.blit(label1, (100, 100))
        screen.blit(label2, (100, 140))
        
        #BLIT MORE LABELS FOR MORE SONG CHOICES
        
        screen.blit(label, (100, 300))
        screen.blit(labelQuit, (100, 340))
        pygame.display.flip()     #end of while loop
        
    pygame.display.quit()    #kills display window
    

main()
    
