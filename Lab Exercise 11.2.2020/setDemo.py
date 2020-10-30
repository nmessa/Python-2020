## Set Demonstration
## Author: nmessa
## This program creates a set of unique numbers
from random import *

numbers = set()
count = 0

while len(numbers) < 10:
    num = randint(1, 20)
    print (len(numbers), numbers)
    count += 1
    numbers.add(num)

print (numbers)
print (count, 'iterations')
