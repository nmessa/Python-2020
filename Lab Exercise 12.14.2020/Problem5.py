## Lab Exercise 12/14/2020 Problem 5
## Author: 
## This program generates Pascal's Triangle
#Create a list that will hold a other lists to become a list of lists
pascal = []

def blank_list_gen(x):
    #create a list of lists of all [0]
    for i in range(x-1):
        pascal.append([0])
##    print(pascal)

def pascals_triangle_generator(rows):   
    blank_list_gen(rows)

    #create lists each containing all 0's
    #Add code here

    
##    print(pascal)
##    print()
    
    #Put a 1 at the beginning and end of each row
    #Add code here
    
##    print(pascal)
##    print()
    
    #Add first two rows of triangle
    #[1]
    #[1, 1]
    #Add code here

    
##    print(pascal)
##    print()
    
    #Calculate values for the rest of the rows
    #Add code here

    
##    print(pascal)
    
pascals_triangle_generator(10)

#Print the triangle
for row in pascal:
    print(row)

## Output
## [1]
## [1, 1]
## [1, 2, 1]
## [1, 3, 3, 1]
## [1, 4, 6, 4, 1]
## [1, 5, 10, 10, 5, 1]
## [1, 6, 15, 20, 15, 6, 1]
## [1, 7, 21, 35, 35, 21, 7, 1]
## [1, 8, 28, 56, 70, 56, 28, 8, 1]
## [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
## [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]
    
