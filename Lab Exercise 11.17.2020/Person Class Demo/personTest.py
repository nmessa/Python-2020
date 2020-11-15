# Program to test the Person class
# Author: nmessa

#import the Person class from person.py
from person import Person

#Create 3 test objects
p1 = Person('Gil Hodges', '12 Main Street', 'Brooklyn', 'NY', '11201')
p2 = Person('Don Drysdale', '2343 Flatbush Boulevard', 'Brooklyn', 'NY', '11201')
p3 = Person('Marion Morrison', '216 South 2nd Street', 'Winterset', 'IA', '50273')

#Print the objects
print (p1)
print (p2)
print (p3)

#test the object methods
p1.changeAddress('1234 Hollywood Boulevard', 'West Hollywood', 'CA', '90069')
p2.changeAddress('4321 Wilshire Boulevard', 'Los Angeles', 'CA', '90020')
p3.changeName('John Wayne')

#print the objects
print (p1)
print (p2)
print (p3)




