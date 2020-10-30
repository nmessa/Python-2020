#Animation demo
#Author: nmessa
#Date: 10.25.2009
#This program draws a moving block.

from graphics import GraphicsWindow
from time import sleep

def main() :
   #Define size of window
   WIN_WIDTH = 400
   WIN_HEIGHT = 400   

   #Create a graphics window
   win = GraphicsWindow(WIN_WIDTH, WIN_HEIGHT)

   #Create a canvas
   canvas = win.canvas()

   #Set fill color to red and clear the canvas
   canvas.setColor("red")
   canvas.clear()
   
   DELAY = 0.01   # 10 milliseconds between frames

   #loop forever
   while True:
      #Create animation
      for frame in range(WIN_WIDTH + 1) :
         draw(canvas, frame)
         sleep(DELAY)
   
   
## Draws a frame on the canvas.
#  @param canvas the canvas on which to draw the frame
#  @param frame which frame as a number
#
def draw(canvas, frame) :
   #define size of block
   BLOCK_WIDTH = 20
   BLOCK_HEIGHT = 20

   #Clear the canvas
   canvas.clear()

   #draw a rectangle
   canvas.drawRect(frame, 0, BLOCK_WIDTH, BLOCK_HEIGHT)


# Start the program.
main()
