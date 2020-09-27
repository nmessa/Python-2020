## Another List Demonstration
## Author: nmessa
## Date: 9.25.2017
## This program demonstrates the difference between printing out a list
## and printing out the items in a list
## This program also demonstrates how to check an object for type

#Create a list
myList = [1, 'one', 2, 'two', 3, 'three', 4, 'four']

#Print the list
print("This is the list:")
print(myList)
print()
print()

#Print the items in the list
print("These are the items in the list")
for item in myList:
    print(item, end = ' ')
print()
print()

#Print the types of items in the list
print("These are the items in the list")
for item in myList:
    print(type(item), end = ' ')
print()
print()

#Print the odd values in the list
print("The items in the list that are odd integers are:")
for item in myList:
    if type(item) is int:
        if item % 2 == 1:
            print(item, end = ' ')
print()
print()

#Print the string values in the list
print("The string items in the list are:")
for item in myList:
    if type(item) is str:
        print(item, end = ' ')
print()
print()
