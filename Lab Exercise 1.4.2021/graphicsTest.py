## Test program to test the Canvas, GeometricObject, Point, Line,
## Rectangle and Circle classes
## Author: nmessa
## Date: 1/4/2021

from canvas import Canvas
from geometricObject import GeometricObject
from point import Point
from line import Line
from rectangle import Rectangle
from circle import Circle
from polygon import Polygon

#Create a canvas to draw on
myCanvas = Canvas(800, 600)

#Create two points
p1 = Point(-100, -100)
p2 = Point(100,100)

#Create a line between the two points
myLine = Line(p1, p2)
myLine.setColor('red')
myCanvas.draw(myLine)

#Create a rectangle from the two points
myRectangle = Rectangle(p1, p2)
myRectangle.setWidth(3)
myRectangle.setColor('blue')
myCanvas.draw(myRectangle)

#Create a circle
myCircle = Circle(p1, 100)
myCircle.setWidth(5)
myCircle.setColor('green')
myCanvas.draw(myCircle)

#Create an octagon
pt = Point(100,100)
pt.setWidth(10)
pt.setColor('red')
myCanvas.draw(pt)
myPoly = Polygon(pt, 8, 50)
myPoly.setWidth(2)
myPoly.setColor('purple')
myCanvas.draw(myPoly)

#Setup exitonclick()
myCanvas.freeze()
