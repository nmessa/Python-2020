## Function demo 1 with plotting
## Author: nmessa
import pylab

ex = []
efx = []

def f(x):
    answer = 3 * x**3 + 7*x**2 - 14*x -12
    return answer


for x in range(-5, 6):
    ex.append(x)
    efx.append(f(x))

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


