## Graphics Drawing Package
## Author: 
## Date: 1/4/2021
## This package consists of a variety of classes that will allow the user
## to easily draw points, lines, rectangles, circles, and polygons.
## A Canvas class is defined that has a draw method which uses the _draw method
## in each GeometricObject class.  Each geometric object (Point, Line, Circle,
## Rectangle, and Polygon) uses the GeometricObject as the base class.

import turtle, math

class Canvas:
    def __init__(self,w,h):
        self.turtle = turtle.Turtle()
        self.screen = turtle.Screen()
        self.width = w
        self.height = h

        self.screen.setup(width=self.width,height=self.height)
        self.turtle.hideturtle()

    def draw(self,gObject):
        self.turtle.up()
        self.screen.tracer(0)
        gObject._draw(self.turtle)
        self.screen.tracer(1)
        
    def freeze(self):
        self.screen.exitonclick()

class GeometricObject:
    def __init__(self):
        self.lineColor = 'black'
        self.lineWidth = 1

    def getColor(self):
        return self.lineColor

    def getWidth(self):
        return self.lineWidth

    def setColor(self,color):
        self.lineColor = color

    def setWidth(self,width):
        self.lineWidth = width

    def _draw(self,someturtle):
        print("Error: You must define _draw in subclass")

class Point(GeometricObject):
    def __init__(self, x,y):
        GeometricObject.__init__(self)
        self.x = x
        self.y = y

    def getCoord(self):
        return (self.x,self.y)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def _draw(self,aturtle):
        #Add code here
        


class Line(GeometricObject):
    def __init__(self, p1,p2):
        GeometricObject.__init__(self)
        self.p1 = p1
        self.p2 = p2
    
    def getP1(self):
        return self.p1
        
    def getP2(self):
        return self.p2
        
    def _draw(self,aturtle):
        #Add code here
        

class Rectangle(GeometricObject):
    def __init__(self, p1,p2):
        GeometricObject.__init__(self)
        self.p1 = p1
        self.p2 = p2
        
    def _draw(self,aturtle):
        #Add code here
        

class Circle(GeometricObject):
    def __init__(self, p1,r):
        GeometricObject.__init__(self)
        self.center = p1
        self.radius = r
        
    def _draw(self,aturtle):
        #Add code here

        

class Polygon(GeometricObject):
    def __init__(self, p1, sides,length):
        GeometricObject.__init__(self)
        self.start = p1
        self.sideLength = length
        self.numsides = sides
        
    def _draw(self,aturtle):
        #Add code here
        

