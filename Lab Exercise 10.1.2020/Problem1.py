##Lab Exercise 10/1/2020 Problem 1
##Author: 
##Print address label

#This function prints an address label
def printLabel(name, address, street, city, state, zipcode, country):
    #Add code here
    

#Get user input for name, address, street, city, state, zipcode, and country
name = input("Enter name: ")
address = input("Enter street number: ")
street = input("Enter street name: ")
city = input("Enter city: ")
state = input("Enter state: ")
zipcode = input("Enter zipcode: ")
country = input("Enter country: ")
print()

#Print the label
printLabel(name, address, street, city, state, zipcode, country)

## Output
## Enter name: Herman Munster
## Enter street number: 13
## Enter street name: Mockingbird Lane
## Enter city: Exeter
## Enter state: NH
## Enter zipcode: 03833
## Enter country: USA
##
## Herman Munster
## 13 Mockingbird Lane
## Exeter NH 03833
## USA
