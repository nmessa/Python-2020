## Lab Exercise 10/22/2020 Problem 3
## Author: 
## This program will display the time using words
## The time will be in five minute intervals

#Create two dictionaries to hold hours and minutes mappings
hours = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five',
          6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten',
          11:'eleven', 12:'twelve'}

minutes = {0:'', 5:'five minutes past',10:'ten minutes past',
           15:'a quarter past', 20:'twenty minutes past',
           25:'twenty five minutes past',30:'half past',
           55:'five minutes until',50:'ten minutes until',
           45:'a quarter to', 40:'twenty minutes before',
           35:'twenty five minutes before'}

#Get time from user and store in myTime in format hh:mm
#Add code here


#Break time into hours and minutes
#store in list t
#Add code here

#Store h and m as an integer from elements of t
#Add code here


#take care of rollover for 12 hour clock
#Add code here


#Print hour and minute phrase
#Add code here



##Sample Output
##Enter the time to the nearest five minutes (hh:mm): 10:05
##five minutes past ten
