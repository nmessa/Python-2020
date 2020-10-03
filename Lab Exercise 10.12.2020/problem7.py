##Lab Exercise 10/12/2020 Problem 7
##Author: 
##Write a program that generates a report card

#this function adds the letter grade to the letterGrades list
def calcLetterGrade(scores):
    #Add code here
    

#this function calculates and returns your GPA given the letterGrades 
#list and the number of classes
def calcGPA(letterGrades, numClasses):
    #Add code here

    

#this function prints your report card
def printReportCard(classes, scores, letterGrades, GPA, numClasses):
    #Add code here



#create 3 global lists
classes = []
scores = []
letterGrades = []

#get the number of classes you are taking
numClasses = int(input("How many classes are you taking? "))

#Enter your classes and scores into data structure (lists)
for i in range(numClasses):  #loop for each class you are taking
    #get the name of class and store in name
    #Add code here


    #get the score you received in the class
    #Add code here


    #add the name of the class to the classes list
    #Add code here


    
    #add the score you received in the class to the scores list
    #Add code here



#put scores into letter grades
#Add code here



#Calculate GPA and store in variable gpa
#Add code here



#Print report card
printReportCard(classes, scores, letterGrades, gpa, numClasses)

## Sample output
## How many classes are you taking? 3
## What is the name of the class? Calculus
## What is the numeric score you received in Calculus: 92
## What is the name of the class? Physics
## What is the numeric score you received in Physics: 81
## What is the name of the class? C++
## What is the numeric score you received in C++: 93
## REPORT CARD:
## Calculus - 92(A)
## Physics - 81(B)
## C++ - 93(A)
## Overall GPA = 3.67
