# Person class definition
# person.py
# Author: nmessa

class Person:
    # constructor method
    def __init__(self, nme, add, cty, st, z):
        self.name = nme
        self.address = add
        self.city = cty
        self.state = st
        self.zip = z

    #method to implement a name change to a Person object
    def changeName(self, nme):
        self.name = nme

    #method to implement an address change to a Person object
    def changeAddress(self, add, cty, st, z):
        self.address = add
        self.city = cty
        self.state = st
        self.zip = z

    #method for printing an object
    def __str__(self):
        s = self.name + '\n' + self.address + '\n' + self.city + ', ' + \
            self.state + '   ' + self.zip + '\n\n'
        return s
