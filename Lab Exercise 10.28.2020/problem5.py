##Lab Exercise 10/28/2020 Problem 5
##Author: 
##This program will find the first 8 Mersenne Primes

from math import *

#This function returns True if passed a prime number
def isPrime(n):
    #Add code here
    

#This function returns True if passed a Mersenne Prime number
def isMersenne(n):
    #Add code here
    

#Create list to hold the Mercenne Prime numbers and the prime number
#that generated them
mersennes = []
numbers = []


#Check numbers from 2 to 1000 to see if they generate a Mersenne Prime
#Hint: consider using continue and break in this loop
for number in range(2,1001):
    #don't test for Mercenne Prime if number is not prime
    #put prime number in list of primes tested
    #leave loop if you have 8 Mercenne Primes


#Print the list showing the Mercenne Prime and the prime
#number that generated it.
for i in range(len(mersennes)):
    print("p =", mersennes[i], "Mersenne Prime Number =", numbers[i])
    

