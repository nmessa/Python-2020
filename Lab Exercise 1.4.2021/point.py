##Point class defintion
##Author: 
##Date: 1.4.2021

from geometricObject import GeometricObject

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
        
