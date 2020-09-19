## Function demo 1
## Author: nmessa

#Function defines f(x)
def fx(x):
    answer = 2 * x**3 - 5*x**2 + 10*x -1
    return answer

for x in range(-5, 6):
    print ('f(' + str(x) + ') = ' + str(fx(x)))

##print (fx(1))
