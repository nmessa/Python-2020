#String Demo
#Author: nmessa
#Date: 10.16.2016
#This will demonstrate several useful string functions

#Split
test = 'this is a test'
result = test.split()
print(result)   # ['this', 'is', 'a', 'test']

test2 = '3/21/2016'
result2 = test2.split('/')
print(result2)  # ['3', '21', '2016']

#join
answer = ' '.join(result)
print(answer) # this is a test

answer2 = '-'.join(result2)
print(answer2)  # 3-21-2016

#string slicing
test3 = 'abcdefg'
slice1 = test3[2:5]  #extract element 2 to 4
print(slice1)   # cde

slice2 = test3[:5]  #extract element 0 to 4
print(slice2)   # abcde

slice3 = test3[2:]  #extract element 2 to end of string
print(slice3)   # cdefg

slice4 = test3[1:6:2]   #extract elements 1, 3, and 5
print(slice4)   # bdf

slice5 = test3[:]       #extract the entire string
print(slice5)   # abcdefg

#reversing a string the easy way
test4 = 'abcdefghijklmnopqrstuvwxyz'
slice6 = test4[::-1]
print(slice6)   # zyxwvutsrqponmlkjihgfedcba

#printing the last element of a string
test5 = 'abc'
last = test5[-1]
print(last)     #c


