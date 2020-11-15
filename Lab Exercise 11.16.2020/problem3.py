#Lab Exercise 11.16.2020 Problem 3
#Author: 
#This program will read lines from the coefficents of a quadratic
#equation from a file coefficients.txt.  The program will find the
#roots of the equation and write them back to roots.txt

from random import *
from math import *

#Define the size of your data to be 1 million
DATA_SIZE = 1000000


##Generates coefficients file
##outFile = open('coefficients.txt', 'w')
##count = 0
##while count < DATA_SIZE:
##    a = randint(-100, 100)/10
##    b = randint(-100, 100)/10
##    c = randint(-100, 100)/10
##    if a != 0:
##        outFile.write(str(a) + ' ' + str(b) + ' ' + str(c) + '\n')
##        count += 1
##outFile.close()

#Open file coefficients.txt to read
#Add code here


#read all lines and store in list lines
#Add code here



#close the file
inFile.close()

#open a file roots.txt to write
#Add code here



#process each line from the file
for line in lines:
    #break apart line into the 3 coefficients
    #Add code here



    #store the 3 coeffieients into variables a, b, and c as float
    #Add code here



    #calculate discriminant
    #Add code here



    #if discriminant is greater than or equal to 0
    #calculate root1 and root2 and write to file
    #if discriminant is negative write "No Real Roots" to file
    #Add code here





#close the file
#Add code here


