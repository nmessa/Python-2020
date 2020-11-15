## Program that will print the decimal equivalents of fractions
## Author: nmessa

# import the Fraction class for fraction.py
from fraction import Fraction

#construct fraction and print decimal equivalent
for i in range(1,32):
    myFraction = Fraction(i, 32)
    print (myFraction, '=', myFraction.decimal)

    

