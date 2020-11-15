## Fraction class definition
## Author: nmessa
## Date: 11/7/2016

class Fraction:
    #constructor method
    def __init__(self, num, den):
        self.numerator = num
        self.denominator = den
        self.reduceFraction()
        self.decimal = num/den

    #method to reduce the Fraction object
    def reduceFraction(self):
        divisor = self.gcd(self.numerator, self.denominator)
        self.numerator //= divisor
        self.denominator //= divisor

    #implement Euclid algorithm - used by reduceFraction
    def gcd(self, a, b):
        remainder = a % b;
        while remainder != 0:
            a = b;
            b = remainder;
            remainder = a % b;
        return b;

    def __str__(self):
        return str(self.numerator) + '/' + str(self.denominator)
