## Lab Exercise 12/10/2020 Problem 4
## Author: 
## Program to test if two balls have collided in 2D and 3D space
from distance import distance3D
from point3D import Point3D

def collide3D(t1, t2):
    # store center and radius of two circles
    #Add code here

    #if the distance between centers is less than the sum
    #of their radius then collision has occured and return True
    #Add code here
    
#Test code
#ball set 1 for 3D space
t1 = (0,0,0, 1)
t2 = (3,3,3, 1)
print (collide3D(t1, t2)) #False

#ball set 2 for 3D space
t1 = (5,5,5,2)
t2 = (2,8,5,3)
print (collide3D(t1, t2))   #True

#Output
1.4142135623730951  #from distance function
1.7320508075688772  #from distance function
False
True
        
    
