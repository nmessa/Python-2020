## Lab Exercise 10/29/2020 Problem 1
## Author: 
## This program contains a function that will calculate the affect of
## air drag on a car
def drag(mph):
    #define and initialize variables v (velocity), density (density of air),
    #area (cross sectional area of front of car)
    #and coefficientDrag(typical drag coefficient)
    #be sure to convert mph to m/s
    #Add code here
    

    #calculate the force of drag and store in fd
    #Add code here
    

    #Calculate power in watts and store in the variable power
    #Add code here
    

    #Convert watts to horsepower and store in variable horsepower
    #Add code here
    

    
    return horsepower

#Create a table showing lost horsepower
for speed in range(0,201,5):
    print ("At", speed, 'MPH', drag(speed), "horsepower is lost")

    
