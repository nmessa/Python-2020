## Lab Exercise 12/10/2020 Problem 6
## Author: 
## Prime Factorization Program
from math import sqrt

def isPrime(number):
    #This function returns True if the integer passed to it is prime
    for i in range(2, int(sqrt(number))):
        if number % i == 0:
            return False
    return True

def factor(number):
    #This function returns a list of prime factors of an integer
    #Add code here
    
number = int(input("Enter a number you want factored: "))
print ("The prime factors are: " + str(factor(number)))

##Sample Output
##Enter a number you want factored: 1234321
##The prime factors are: [11, 11, 101, 101]
