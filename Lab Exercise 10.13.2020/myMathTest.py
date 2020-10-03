##Lab Exercise 10.13.2020
##Author: nmessa
import myMath

#Get radius of sphere and stroe as a float in variable radius
radius = float(input("Enter the radius of a sphere: "))

#Get length, width, and height of cuboid and store in string temp
temp = input("Enter the length, width, and height of a cuboid: ")

#break apart string into the strings length, width, and height
length, width, height = temp.split()

#Convert the strings length, width, and height into float values
length = float(length)
width = float(width)
height = float(height)

#Define coefficients of polynomial
poly = [5, 3.2, 7.1, 0, 6.9]

#define a value for x
x = -13

#Test module functions
print ("Surface area of sphere = ", myMath.sphereArea(radius))
print ("Volume of sphere = ", myMath.sphereVolume(radius))
print ("Surface area of cuboid = ", myMath.cuboidArea(length, width, height))
print ("Volume of cuboid = ", myMath.cuboidVolume(length, width, height))
print (myMath.polyPrettyPrint(poly), '=', myMath.evaluatePoly(poly, x))

