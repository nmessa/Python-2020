## Demo problem 2
## Author: nmessa
## Date 12.16.2015
##
## 2x + 3y + 4z = 119
## 5x - 6y + 7z = 80
## 8x + 9y + 10z = 353

from pylab import *

M = array([[2, 3, 4], [5, -6, 7], [8, 9, 10]])
V = array([119, 80, 353])

print (solve(M, V))
