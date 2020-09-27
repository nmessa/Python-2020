##Using pyplot to plot some data
##Author: nmessa
##Date: 9.25.2017

import matplotlib.pyplot as plt
#two lists to define x and y values
x = [1,2,3]
y = [4,5,6]
plt.plot(x, y)
plt.grid(True)
plt.ylabel('some numbers')
plt.show()
