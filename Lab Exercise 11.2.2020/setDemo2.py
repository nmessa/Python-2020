## List Demonstration
## Author: nmessa
## This program creates a "set" of unique numbers
from random import *

numbers = list()
count = 0

while len(numbers) < 10:
    num = randint(1, 100)
    if num not in numbers:
        numbers.append(num)
        print (len(numbers), numbers)
    count += 1

print (numbers)
print (count, 'iterations')
