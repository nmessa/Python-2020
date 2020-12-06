#Lab Exercise 12/9/2020 Problem 2 - Skeleton
#Author: 
#fraction.py
#implementation of Fraction class

class Fraction:
    def __init__(self, num, den):
        #ADD CODE HERE
        
        
    def reduce(self):
        #ADD CODE HERE
        

    def gcd(self, a, b):
        #ADD CODE HERE
        

    def __str__(self):
        #ADD CODE HERE
        

    def add(self, other):
        n = self.num * other.den + other.num * self.den
        d = self.den * other.den
        temp = Fraction(n, d)
        return temp

    def subtract(self, other):
        #ADD CODE HERE

    def multiply(self, other):
        #ADD CODE HERE

    def divide(self, other):
        #ADD CODE HERE

#Code to test the Fraction class
f1 = Fraction(1, 2)
f2 = Fraction(3, 4)
print (f1)
print (f2)
f3 = Fraction(6, 8)
print (f3)
f4 = f1.multiply(f2)
f5 = f1.add(f2)
f6 = f1.subtract(f2)
f7 = f1.divide(f2)

print (f1, '*', f2, '=', f4)
print (f1, '+', f2, '=', f5)
print (f1, '-', f2, '=', f6)
print (f1, '/', f2, '=', f7)

        
