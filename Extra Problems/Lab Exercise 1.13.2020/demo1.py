## Demo problem 1
## Author: nmessa
## Date 12.16.2015
##
## 2x + 3y = 10
## 3x - y = -1.5

from pylab import *

M = array([[2, 3], [3, -1]])
V = array([10, -1.5])

print (solve(M, V))
