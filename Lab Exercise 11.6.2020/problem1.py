##Lab Exercise 11/6/2020 Problem 1
##Author: 
##This program draws a moving block.
##It moves from upper left to lower right

from graphics import GraphicsWindow
from time import sleep

def main() :
   #define window size
   #Add code here

   

   #create a graphics window
   #Add code here



   #create a canvas
   #Add code here



   #set color to red and clear canvas
   #Add code here


   
   DELAY = 0.01   # 10 milliseconds between frames

   #animate the frame from upper left corner (0,0)
   #to lower right corner (WIN_WIDTH, WIN_WIDTH)
   #Add code here


   
   win.wait()
   
## Draws a frame on the canvas.
#  @param canvas the canvas on which to draw the frame
#  @param frame which frame as a number
#
def draw(canvas, frame) :
   #define vlock size
   #Add code here



   #clear the canvas
   #Add code here



   #draw a rectangle at (frame, frame) with a width and height of
   #BLOCK_WIDTH and BLOCK_HEIGHT
   #Add code here




# Start the program.
main()
