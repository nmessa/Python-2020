##Graphics Demo
##Author: nmessa
##Date: 10/3/2017

from graphics import GraphicsWindow

win = GraphicsWindow(800, 800)

canvas = win.canvas()

#Draw a rectangle
#drawRect(x, y, width, height)
canvas.drawRect(100, 100, 200, 100)

#draw a line
##drawLine(x1, y1, x2, y2)
canvas.drawLine(0,0,799,799)

#draw a filled rectangle
canvas.setOutline("yellow")
canvas.setFill("red")
canvas.setLineWidth(20)
canvas.drawRect(500, 300, 100, 200)

#draw an oval
canvas.setOutline("red")
canvas.setFill("green")
canvas.setLineWidth(10)
canvas.drawOval(300, 475, 200, 300)


#draw a circle
canvas.setOutline(100, 200, 100)
canvas.setFill(200, 100, 200)
canvas.setLineWidth(20)
canvas.drawOval(50, 250, 300, 300)

#draw another circle
canvas.setColor("red")
canvas.drawOval(450, 50, 300, 300)

#wait for user to close window
win.wait()
