##Lab Exercise 10/28/2020 Problem 4
##perfect.py
##Author: 
##Date: 10/28/2020
##This program finds all of the perfect numbers <= 10000

#This function returns True if integer sent to it is a perfect number
#and returns False if it is not
def isPerfect(n):
    #Add code here
    

#Test all numbers frm 1 to 10000 for perfection
#Print only the numbers that are perfect
for number in range(1, 10001):
    if(isPerfect(number)):
        print(number, end = ' ')

 


        
