## Lab Exercise 11/6/2020 Problem 3
## Author: 
## This program will merge two lists

def mergeSorted(a, b):   #a and b are lists
   #set index for each list
   i = 0
   j = 0

   #create empty list
   sortedList = []

   #merge the lists until one is empty
   while i < len(a) and j < len(b):
      #Add code here

      

   #when a list is empty append the elements of the non-empty list
   if i == len(a):   #list a went empty
      for index in range(j, len(b)):
         sortedList.append(b[index])
         
   if j == len(b):   #list b went empty
      #Add code here

      


   #return the merge sorted list
   return sortedList

#code to test the function
a = [1,4,9,16]
b = [4,7,9,9,11]
print (mergeSorted(a, b)) #[1, 4, 4, 7, 9, 9, 9, 11, 16]
         
      
