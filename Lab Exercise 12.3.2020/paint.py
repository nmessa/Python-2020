## Lab Exercise 12/3/2020 - Paint Program
## Author: 
## A basic painting program that draws basic shapes as well as
## freehand drawing

import pygame, sys

def main():
    #Initialize Pygame
    #Add code here
    

    #Setup the screen
    #Add code here
    
    
    #Create a background to draw on
    background = pygame.Surface(screen.get_size())

    #Make background white
    background.fill((255, 255, 255))

    #Create a clock
    #Add code here
    

    #Initialize variables
    #Add code here
    
    
    #Start game loop
    while keepGoing:
        #Set clock rate
        #Add code here
    

        #Check events
        for event in pygame.event.get():
            #Quit event
            #Add code here
    
                
            #MOUSEMOTION event
            elif event.type == pygame.MOUSEMOTION:
                #Store mouse position in lineEnd
                #Add code here
    

                #Draw a line if left mouse button is pressed
                #Add code here

    
                #Store lineEnd in lineStart
                #Add code here
    

            #KEYDOWN event    
            elif event.type == pygame.KEYDOWN:
                #place myData into a tuple to be passed to checkKeys
                #Add code here
    

                #Call checkKeys and store returned tuple in myData
                #Add code here
    

                #unpack myData tuple
                #Add code here
    

        #BLIT background
        #Add code here
    

        #Call showStats and store returned result in myLable
        #Add code here
    

        #BLIT myLabel
        #Add code here
    

        #flip the display
        #Add code here
    
        
    #End program    
    #Add code here
    
    
def checkKeys(myData):
    #Define filename to store bitmapped image
    filename = 'myPainting.bmp'
    
    """test for various keyboard inputs"""
    #extract the data from myData tuple
    #Add code here
    

    if event.key == pygame.K_q:
        #quit
        #Add code here
    
    elif event.key == pygame.K_c:
        #clear screen
        #Add code here
    
    elif event.key == pygame.K_s:
        #save picture
        #Add code here
    
    elif event.key == pygame.K_l:
        #load picture
        #Add code here
    

    #colors
    elif event.key == pygame.K_r:
        #red
        drawColor = (255, 0, 0)
    elif event.key == pygame.K_g:
        #green
        #Add code here
    
    elif event.key == pygame.K_w:
        #white
        #Add code here
    
    elif event.key == pygame.K_b:
        #blue
        #Add code here
    
    elif event.key == pygame.K_k:
        #black
        #Add code here
    

    #line widths
    elif event.key == pygame.K_1:
        #line width set to 1
        #Add code here
    
    elif event.key == pygame.K_2:
        #line width set to 2
        #Add code here
    
    elif event.key == pygame.K_3:
        #line width set to 3
        lineWidth = 3
    elif event.key == pygame.K_4:
        #line width set to 4
        #Add code here
    
    elif event.key == pygame.K_5:
        #line width set to 5
        #Add code here
    
    elif event.key == pygame.K_6:
        #line width set to 6
        #Add code here
    
    elif event.key == pygame.K_7:
        #line width set to 7
        #Add code here
    
    elif event.key == pygame.K_8:
        #line width set to 8
        #Add code here
    
    elif event.key == pygame.K_9:
        #line width set to 9
        #Add code here
    

    #Package data into tuple myData 
    #Add code here
    
    
    #return all values
    #Add code here
    

def showStats(drawColor, lineWidth):
    #shows the current statistics (lineWidth and drawColor)
    #Add code here
    

main()
