## Function demo 4
## Author: nmessa 
from pylab import *

#Function defines f(x)
def f(x):
    answer = 2 * x**3 - 5*x**2 + 10*x -1
    return answer

ex = []
fx = []

for x in range(-500, 500):
    value = x/100.0
    ex.append(value)
    fx.append(f(value))

grid(True)
plot(ex, fx)
show()
    

##print (f(1))
