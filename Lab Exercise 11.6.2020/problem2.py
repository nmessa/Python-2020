## Lab Exercise 11/6/2020 Problem 2
## Author: 
## This program will have a red block bouncing from upper left to
## lower right corner

from graphics import GraphicsWindow
from time import sleep

def main() :
   #define window size
   #Add code here

   

   #create a graphics window
   #Add code here



   #create a canvas
   #Add code here



   #det color to red and clear the canvas
   #Add code here


   
   DELAY = 0.01   # 10 milliseconds between frames

   while True:
      #move block from upper left to lower right
      #Add code here



      #move block from lower right to upper left
      #Add code here



   win.wait()
   
## Draws a frame on the canvas.
#  @param canvas the canvas on which to draw the frame
#  @param frame which frame as a number
#
def draw(canvas, frame) :
   #define block size
   #Add code here



   #clear the canvas
   #Add code here



   #draw a rectangle at (frame, frame) with a width and height
   #of BLOCK_WIDTH and BLOCK_HEIGHT
   #Add code here




# Start the program.
main()
