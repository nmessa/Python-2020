## Function Demo 2
## Author: nmessa

#function to determine if an integer is prime
def isPrime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


#Test code
print (isPrime(9))          #False
print (isPrime(17))         #True
print (isPrime(1234567654321))    #False
