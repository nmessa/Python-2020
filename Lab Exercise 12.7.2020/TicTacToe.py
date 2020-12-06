##Lab Exercise 12.7.2020
##Author: nmessa
##File: TicTacToe.py
#improved drawing location of X's and O's

import pygame, time

#This function will draw an X at a specified location
def drawX(x, y):
    #create a map for drawing 25 rectangles
    #1 = black rectangle
    #0 = white rectangle
    x_list = [[1,0,0,0,1],
              [0,1,0,1,0],
              [0,0,1,0,0],
              [0,1,0,1,0],
              [1,0,0,0,1]]
    #set height and width of rectangles
    width = 30
    height = 30

    #store the original x value
    ex = x

    #draw a 5 x 5 array of 30 pixel x 30 pixel rectangles
    for row in range(5):
        for col in range(5):
            #determine if rectangle is going to be red or white
            if x_list[row][col]:
                color = [255,0,0]
            else:
                color = [255, 255, 255]
            #draw the rectangle
            pygame.draw.rect(screen, color, [x,y, width, height])
            #update x position for next rectangle
            x += width
        #update y position for next row of rectangles
        y += height
        #reset x position for next row
        x = ex

#This function will draw an O at a specified location
def drawO(x, y):
    #Add code here


    

def drawLines():
    #Draw lines for Tic-Tac-Toe board
    #Add code here


    
def showState():
    #this function is used for testing
    #Add code here



def resetState():
    #Add code here


            
def resetGame():
    #Add code here



#This function determines if a win has occured and which player won
#This is done by checking the contents of the state array
def checkWin():
    #column 1
    if state[0][0] == state[1][0] and state[1][0] == state[2][0]:
        if state[0][0] + state[1][0] + state[2][0] == 3:
            #Player X won
            pygame.draw.line(screen, [255,0,0],[100,0], [100, 600], 10)
            return True
        elif state[0][0] + state[1][0] + state[2][0] == 6:
            #Player O won
            pygame.draw.line(screen, [0,255,0],[100,0],[100, 600], 10)
            return True

    #column 2
    #Add code here



    #column 3
    #Add code here



    #row 1
    #Add code here



    #row 2
    #Add code here



    #row 3
    #Add code here



    #diagonal 1
    #Add code here



    #diagonal 2
    #Add code here



    return False #Game not yet won

#main program       
#initialize pygame    
#Add code here



#set counter to keep track of whose turn
#Add code here



#keep track of state of board - used to check who won
#Add code here



#set the drawing screen to 600 x 600
screen = pygame.display.set_mode([600,600])
pygame.display.set_caption("Tic-Tac_Toe")

#fill the screen with white
#Add code here



#draw the lines for the tic-tac-toe board
#Add code here



#Create flag variable for ending game loop
#Add code here



#Game loop
while not quit:
    #Check all pygame events
    for event in pygame.event.get():
        #quit event
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
        #KEYDOWN events
        elif event.type == pygame.KEYDOWN:
            #clear board event
            if event.key == pygame.K_c:
                #Add code here


            #display the state of board
            elif event.key == pygame.K_s:
                #Add code here


        #MOUSEBUTTON event
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1, 0, 0):
                #get position of mouse click and convert to list
                #Add code here


                
                #Determine row and column selected
                #Add code here


                
                #Adjust x position to properly position X or O
                #Add code here


                    
                #Adjust y position to properly position X or O
                #Add code here


                
                #update turn for next player
                #Add code here



                #Player turn
                #draw X or O
                #Update state array
                #Check for win
                if turn%2:
                    #Add code here


                else:
                    #Add code here



                #update display
                pygame.display.flip()

time.sleep(4)
pygame.display.quit()
            
