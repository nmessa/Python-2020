#String index and slicing demonstration
#Author: nmessa
#Date: 10.2.2007

s = 'Hello World'

#print the length of the string
print (len(s))

#print the last element of the string (2 ways)
print (s[len(s) - 1])
print()
print (s[-1])

#String slicing has the form s[start:end + 1]

#print the last 3 characters in the string
print (s[-3:])

#print the first 3 characters in the string (2 ways)
print (s[0:3])
print (s[:3])

print (s[2:8]) #prints 'llo Wo'

