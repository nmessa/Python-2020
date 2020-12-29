## Program to demonstrate sets in Python
## Author: nmessa
## Date: 12/6/2015

import random
numbers = set([])  #set to hold numbers

SIZE = 10
count = 0

#generate set of 10 random numbers without duplicates 
while len(numbers) < 10:
    numbers.add(random.randint(1,SIZE))
    count += 1

#convert set to a list
numbers = list(numbers)

for i in range(len(numbers)):
    print (numbers[i], end = ' ')
    
print()   
print (count, 'tries to fill the set')


    

    
