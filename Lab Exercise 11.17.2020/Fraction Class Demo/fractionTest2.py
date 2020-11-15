## Test program to test the Fraction class
## Author: nmessa

# import the Fraction class for fraction.py
from fraction import Fraction
from random import *

fractions = []

#create a thousand fractions and put them in a list
for i in range(1000):
    temp = Fraction(randint(1, 100), randint(1,100))
    fractions.append(temp)
    

#print the Fraction objects
for i in range(len(fractions)):
    print (fractions[i], end = ' ')
    if i % 10 == 0:
        print()
