#import matplotlib.pyplot as plt    # import a plotter
from pylab import *
#plt.suptitle("This is the title", size=16)  # set upper title
xvals = list(range(10))                     # make list of x values
yvals = [x**2 for x in xvals]     # make list of y values
plot(xvals, yvals, 'r')       # plot x,y in red
show()                       # Output plot via TK
