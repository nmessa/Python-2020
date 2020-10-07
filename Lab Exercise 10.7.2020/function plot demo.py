## Function demo 1 with plotting
## Author: nmessa
from pylab import *

#Create 2 empty lists to hold x and f(x) values
ex = []
efx = []

#Define a function
def f(x):
    answer = 3 * x**3 + 7*x**2 - 14*x -12
    return answer

#Generate 11 points from -5 to 5
for x in range(-5, 6):
    ex.append(x)
    efx.append(f(x))

#Plot the function
plot(ex, efx)
xlabel("x")
ylabel("f(x)")
grid(True)
show()


#This code will generate a smoother graph

#Create 2 empty lists to hold x and f(x) values
ex1 = []
efx1 = []

#Generate 1001 points from -5.00 to 5.00
x = -5.0
while x <= 5:
    ex1.append(x)
    efx1.append(f(x))
    x += 0.01
    
#Plot the function
plot(ex1, efx1)
xlabel("x")
ylabel("f(x)")
grid(True)
show()  


