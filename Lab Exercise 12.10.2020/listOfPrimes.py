## Lab Exercise 12/10/2020 Problem 5
## Author: 
## Prime List
from math import sqrt

def isPrime(number):
    #This function returns True if integer passed to it is prime
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def listOfPrimes(number):
    #Add code here
    
    
number = int(input("Enter the largest prime to check: "))
print ("The prime numbers are: " + str(listOfPrimes(number)))
