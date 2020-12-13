## Lab Exercise 12/14/2020 Problem 4
## Author: 
## Calculates the area of a triangle
from math import sqrt

#Determines whether or not a valid triangle exists
def isTriangle(a, b, c):
    #Add code here
    

#Calculates the are of a triangle using Heron's Method if valid triangle
def calcArea(a, b, c):
    if not isTriangle(a,b,c):
        return "Not a valid triangle"
    #Add code here
    

#Test code
a = 3
b = 4
c = 5
print (calcArea(a, b, c))     #6.0

a = 3
b = 5
c = 10
print (calcArea(a, b, c))     #Not a valid triangle
