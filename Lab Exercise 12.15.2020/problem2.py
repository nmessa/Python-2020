## Lab Exercise 12/15/2020 Problem 2
## Author: 
## This program simulates a random walk and determines the distance
## the turtle ends up from home

from turtle import *
import random, time

def randomWalk(t, steps, distance = 20):
    #Add code here
    

bob = Turtle()
dist = randomWalk(bob, 100)
print ('The turtle wandered', round(dist,2), 'units from the origin')
time.sleep(5)
bye()
