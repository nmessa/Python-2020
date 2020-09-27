## Function demo 1 with plotting
## Author: nmessa
import pylab

ex = []
efx = []

def f(x):
    answer = 3 * x**3 + 7*x**2 - 14*x -12
    return answer

#plot range from -5 to 5
#use 1000 points
x = -5
for i in range(1000):
    ex.append(x)
    efx.append(f(x))
    x += 10/1000

pylab.plot(ex, efx)
pylab.grid(True)
pylab.show()






##ex1 = []
##efx1 = []
##x = -5.0
##while x <= 5:
##    ex1.append(x)
##    efx1.append(fx(x))
##    x += 0.01
##
##pylab.plot(ex1, efx1)
##pylab.grid(True)
##pylab.show()   


