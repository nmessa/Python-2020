## Function Demo 3
## Author: nmessa
## Prints all prime numbers under 1000

def isPrime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


for num in range(2, 1001):
    if isPrime(num):
        if num % 5 == 0:
            print()
        print (num , end = ' ')
