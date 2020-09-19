##Lab Exercise 9/29/2020 Problem 4
##Author: 
##This program provide multipliction drill problems

import random

#Get the number of problems in the drill from user as an integer
#Add code here


#Set correct counter variable to 0
#Add code here



#Run the drill
for i in range(problems):
    #Generate 2 random integers and store in variables num1 and num2
    #Add code here



    # Print problem
    print (num1, 'x', num2, '= ? ',)

    #Get user answer and store in variable answer
    answer = int(input())


    #check user answer
    if answer == num1 * num2:
        #Print correct message and increment correct counter
        #Add code here


    else:
        #Print incorrect message
        #Add code here



#calculate percentage correct as a floasting point number
#store in variable percentage
#Add code here



#round the percentage correct to 2 decimal places
#Add code here



#Determnine letter grade
#Add code here



#print results
print (str(percentage) + "% = " + grade)

## Output
## How many problems do you wish to try? 3
## 6 x 3 = ?
## 18
## correct
## 2 x 10 = ?
## 20
## correct
## 5 x 12 = ?
## 60
## correct
## 100.0 % = A
