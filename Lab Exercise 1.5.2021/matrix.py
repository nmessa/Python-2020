## Program to demonstrate a 2D array (aka a list of lists)
## Author: nmessa
## Date: 12/5/2016 

import random
#create a 2D matrix initialized to 0 using list comprehension
map = [[0 for x in range(5)] for x in range(5)]

#open data file for reading
infile = open("map.dat", 'r')

#fill the array
for row in range(5):
    for col in range(5):
        map[row][col] = int(infile.readline())

#Close the file
infile.close()

#print the array
for row in range(5):
    for col in range(5):
        print (map[row][col], end = ' ')
    print()
    
##Output
##34 21 32 41 25 
##14 42 43 14 31 
##54 45 52 42 23 
##33 15 51 31 35 
##21 52 33 13 23
