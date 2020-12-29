## Lab Exercise 1/5/2021 Problem 2
## Author: 
## This program will hunt for treasure using a map

import random

def searchForTreasure(row, col):
    #Get value from map
    #remember row and col are 0-based
    #Add code here
    

    #if treasure is found
    if value == row*10 + col:
        #print where you found the treasure
        #Add code here

    
    #if treasure not found
    else:
        #find row and col of next location
        #Add code here
    

        #print next location
        #Add code here

        #call searchForTreasure function using new row and col
        #Add code here
    

        
#create a 2D matrix initialized to 0 using a list comprehension
#Add code here
    

#open data file (map.dat) for reading
#Add code here
    

#Fill the matrix with values read from a file
#Add code here
    

#Close the data file
#Add code here
    

##Print out the map
##for row in range(5):
##    for col in range(5):
##        print( map[row][col], end = ' ')
##    print()

#Start search and location(1, 1)
searchForTreasure(1,1)

##Output
##Going to location (3, 4)
##Going to location (4, 2)
##Going to location (1, 5)
##Going to location (2, 5)
##Going to location (3, 1)
##Going to location (5, 4)
##Going to location (1, 3)
##Going to location (3, 2)
##Going to location (4, 5)
##Going to location (3, 5)
##Going to location (2, 3)
##Going to location (4, 3)
##Going to location (5, 1)
##Going to location (2, 1)
##Going to location (1, 4)
##Going to location (4, 1)
##Going to location (3, 3)
##Going to location (5, 2)
##You have found the treasure at (5, 2)
