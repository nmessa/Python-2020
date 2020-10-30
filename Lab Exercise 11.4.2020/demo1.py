## File demo program
## Author: nmessa
## This program generates random temperatures and writes them to a file
## The program then reads in the temperatures and calculates the average
from random import *

#write 100 temperatures to a file
myFile = open('temps.txt','w')
for i in range(100):
    temp = randint(30, 90)
    myFile.write(str(temp) + ' ')  #must be written as a string
myFile.close()

total = 0

myFile = open('temps.txt', 'r')
temps = myFile.read()  #read in the temperatures (all on same line)
myFile.close()
print(temps)
print()

##
#make a list of strings
print('\n\n\nHere is the list')
temps = temps.split()
print(temps)
print()

##
#make a list of numbers
tempValues = []
for i in range(len(temps)):
    tempValues.append(int(temps[i]))
print(tempValues)
print()

average = sum(tempValues)/len(tempValues)


print ("The average temperature is", average, 'degrees Fahrenheit' )

##
##
