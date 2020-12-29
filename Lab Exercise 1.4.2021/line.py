##Line class definition
##Author: 
##Date: 1/4/2021

from geometricObject import GeometricObject

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
        
