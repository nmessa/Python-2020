""" playSong.py
    demonstrates playing an ogg sound
    on demand """

import pygame
pygame.init()
pygame.mixer.init()

def main():
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Play song")
    
    #create background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 0))
    
    #create label
    myFont = pygame.font.SysFont("None", 30)
    label = myFont.render("Press SPACE to hear a song", 1, (0, 0, 255))
    label2 = myFont.render("Press ESC key to exit", 1, (0, 0, 255))
    
    #create sound
    mySong = pygame.mixer.Sound("song1.ogg")
    
    keepGoing = True
    clock = pygame.time.Clock()
    
    while keepGoing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    mySong.play()
                elif event.key == pygame.K_ESCAPE:
                    pygame.mixer.stop()
                    keepGoing = False
    
        screen.blit(background, (0, 0))
        screen.blit(label, (100, 100))
        screen.blit(label2, (100, 140))
        pygame.display.flip()
    pygame.display.quit()    #kills display window

main()
    
