## Lab Exercise 1/5/2021 Problem 1
## Author: 
## Generate a list of prime numbers and Fibonacci numbers found in
## a random set of numbers

import random, math
numbers = set([])  #set to hold 1000 unique random numbers
primes = []         #holds a list of all prime numbers up to SIZE
fibonacci = [0, 1]  #holds a list of Fibonacci numbers up to SIZE
primeList = []      #holds a list of prime numbers found in numbers
fibonacciList = []  #holds a list of Fibonacci numbers found in numbers
SIZE = 10000

def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

#generate list of 1000 random numbers without duplicates (use a set)
#each number in the list should have a value of 1 to 10000
#Add code here


#turn set into a list
#Add code here


#build Fibonacci number list of all Fibonacci numbers up to SIZE
#Add code here


#build prime number list of all prime numbers up to SIZE
#Add code here


#Make list of Fibonacci numbers found in numbers
#Add code here


#Make list of Prime numbers found in numbers
#Add code here


print ("Primes =", primeList)
print ("Fibonacci numbers", fibonacciList)
    

    
