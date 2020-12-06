#Point class definition
#Author nmessa
#Date: 12/10/2020
#This class may be used anyplace that requires a Point with coordinates (x, y)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'



