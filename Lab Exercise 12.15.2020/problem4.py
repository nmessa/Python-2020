## Lab Exercise 12/15/2020 Problem 4
## Author: 
## This program simulates a random walk and determines the maximum
## distance the turtle travels from home.  

from turtle import *
import random, time

#This function returns the maximum distance the Turtle wandered
#from home during it's walk
def randomWalk(t, steps, distance = 20):
    #Add code here
    

#Create a Turtle object
bob = Turtle()
bob.shape("turtle")
maxDistance = randomWalk(bob, 100)
print ("Maximum distance away from home", round(maxDistance,2))
time.sleep(5)
bye()

