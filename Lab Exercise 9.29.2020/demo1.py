## Lab Exercise 9.19.2017 Demo Program 1
## Author: nmessa
## This program will print a table of squares, cubes and square roots
## of the integers from 1 to 10
from math import *

#Print heading
print("X", "\t", "X^2", "\t", "X^3", "\t", "sqrt(x)")

#Print table
for x in range(1, 11):
    #calculate values for square, cube, and square root of number
    square = x**2
    cube = x**3
    square_root = sqrt(x)

    #round the values to 2 decimal places
    square = round(square,2)
    cube = round(cube, 2)
    square_root = round(square_root, 2)

    #print the values
    print(x, "\t", square, "\t", cube, "\t", square_root)

#Output
## X 	 X^2 	 X^3 	 sqrt(x)
## 1 	 1 	 1 	 1.0
## 2 	 4 	 8 	 1.41
## 3 	 9 	 27 	 1.73
## 4 	 16 	 64 	 2.0
## 5 	 25 	 125 	 2.24
## 6 	 36 	 216 	 2.45
## 7 	 49 	 343 	 2.65
## 8 	 64 	 512 	 2.83
## 9 	 81 	 729 	 3.0
## 10 	 100 	 1000 	 3.16
