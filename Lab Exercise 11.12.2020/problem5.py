## Lab Exercise 11/12/2020 Problem 5
## Author: 
## This program removes the middle of the list
## If the length of the list is odd remove the middle element
## If the length of the list is even remove the middle two elements

def removeMiddle(lst):
    if len(lst) % 2 == 1:
        #Add code here
        
        return lst
    else:
        #Add code here

        
        return lst
        

#Code to test the function
oddList = [1,2,3,4,5,6,7,8,9]
print (oddList)
print (removeMiddle(oddList))
evenList = [1,2,3,4,5,6,7,8,9,10]
print (evenList)
print (removeMiddle(evenList))

## Output
## [1, 2, 3, 4, 5, 6, 7, 8, 9]
## [1, 2, 3, 4, 6, 7, 8, 9]
## [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
## [1, 2, 3, 4, 7, 8, 9, 10]

