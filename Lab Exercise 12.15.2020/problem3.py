## Lab Exercise 12/15/2020 Problem 3
## Author: 
## This program simulates a random walk and determines the distance
## the turtle ends up from home.  3 trials are run and the average
## distance is computed

from turtle import *
import random, time
NUM_TRIALS = 3


def randomWalk(t, steps, distance = 20):
    #Add code here
    

#Create a list to hold the distance wandered each trial
distances = []

#Create a Turtle object
#Add code here

#Run the experiment NUM_TRIALS times
#Reset the Turtle to it's home position after each trial
#Be sure to clear the Turtle each trial and put penup before
#moving Turtle to home position and putting pendown after
#getting to the home position
for i in range(NUM_TRIALS):
    #Add code here
    

#Calculate the average distance Turtle wandered for NUM_TRIALS trials
#Add code here

#Print result of the experiments
print (distances)
print ("The average distance the turtle ended up away from home =",
       round(average,2))
bye()
