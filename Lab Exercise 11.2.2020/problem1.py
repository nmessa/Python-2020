## Lab Exercise 11/2/2020 Problem 1
## Author: 
## This program tests if lists are equal

def equals(a, b):
    #Add code here

    

#test suite
a = [1, 2, 3, 4]
b = [1, 2, 3, 4]
print (equals(a, b))  #True

a = [1, 2, 5, 4]
b = [1, 2, 3, 4]
print (equals(a, b))  #False

a = [1, 2, 3, 4]
b = [5, 2, 3, 4]
print (equals(a, b))  #False

a = [1, 2, 3]
b = [1, 2, 3, 4]
print (equals(a, b))  #False


