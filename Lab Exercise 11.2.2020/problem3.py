## Lab Exercise 11/2/2020 Problem 3
## Author: 
## This program generates all permutations of the 5 flavors of ice cream
## choosing 3 at a time

from random import *

#Create an empty list to hold permutations
#Add code here


#Create a list to hold 5 flavors of ice cream
#Add code here


#Create an empty list to hold the sundaes
#Add code here


count = 0 #keep track to the number of sundaes in the permutation list
count2 = 0 #keep track of the number of flavors added to sundae


while count < 60:
    #generate a sundae
    while count2 < 3:
        #Add code here


        
    #reset count2 to generate the next sundae
    count2 = 0

    #Add sundae to permutationList if not already in list and add 1 to count
    #Add code here


    
    #reset the sundae list for the next sundae
    sundae = []

#Print the sundaes
for i in range(len(permutationList)):
    print(permutationList[i])
    
#print(sundae) #for testing purposes



