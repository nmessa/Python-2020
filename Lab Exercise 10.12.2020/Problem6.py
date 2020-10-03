##Lab Exercise 10/12/2020 Problem 6
##Author: nmessa
##Simulates Collatz sequence
import random

#implements the hailstone sequence
def collatz(number):
    #if number is even integer divide by 2 and return the new number
    #else multiply the number by 3, add 1 and return the new number
    #Add code here

    

#test code
    
number = 101
while number != 1:  #keep looping until number gets to 1
    #Pass the number to collatz function and store returned value in number
    #Add code here



    #Print the new number
    print (number, end = ' ')

## Output with number = 101
## 304 152 76 38 19 58 29 88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
