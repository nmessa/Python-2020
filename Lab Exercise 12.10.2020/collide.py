## Lab Exercise 12/10/2020 Problem 3
## Author: 
## Program to test if two balls have collided

from distance import distance
from point import Point

def collide(t1, t2):
    # store center and radius of two circles
    #Add code here
    
    #if the distance between 2 points is less than the sum
    #of their radius then collision has occured and return True
    #Add code here
    

#Test code
#ball set 1
t1 = (0,0,1)
t2 = (3,3,1)
print (collide(t1, t2)) #False

#ball set 2
t1 = (5,5,2)
t2 = (2,8,3)
print (collide(t1, t2))   #True
        
    
