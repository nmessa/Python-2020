## Graphics Demo
## Author: nmessa
## Date: 10.1.2017
#  This program creates a graphics window with a rectangle. It provides the
#  template used with all of the graphical programs used in the book.
#

from graphics import GraphicsWindow

# Create the window and access the canvas.
win = GraphicsWindow()
canvas = win.canvas()

# Draw on the canvas.
canvas.drawRect(5, 10, 20, 30)

# Wait for the user to close the window.
win.wait()
