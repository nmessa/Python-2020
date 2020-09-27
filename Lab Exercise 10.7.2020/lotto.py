#Powerball numbers generator
#Author: nmessa
#Date: 9.24.2019
#This program generates a Powerball number in accoredance
#with the rules of Powerball
#The rules require the user to pick 5 unique values from 1 to 69
#The user then picks a Powerball with is a number from 1 to 26

from random import *
#Create an empty list
lotto = []

#Generate 5 unique numbers from 1 to 69
while len(lotto) < 5:
    number = randint(1,69)
    if number not in lotto:
        lotto.append(number)

#Sort your numbers list
lotto.sort()

#Print your numbers
print("Your numbers are:")
for num in lotto:
    print(num, end = ' ')
print()

#Generate the Powerball (1 - 26)
powerBall = randint(1,26)

#Print your Powerball
print("The Powerball is:", powerBall)

#Sample output
##Your numbers are:
##2 11 22 25 41 
##The Powerball is: 9
