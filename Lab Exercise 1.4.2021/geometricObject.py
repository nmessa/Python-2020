##GeometricObject class definition
##Author: nmessa
##Date: 1/4/2021

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
