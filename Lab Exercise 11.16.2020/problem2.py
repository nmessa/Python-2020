#Lab Exercise 11.16.2020 Problem 2
#Author: 
#This program will read lines from regular.txt filter out the short words
#and write back words greater than 2 characters to a file shorter.txt

#Open file regular.txt to read
#Add code here


#read all lines and store in list lines
#Add code here


#close the file
#Add code here


#open a file shorter.txt to write
#Add code here


#process each line from the file
for line in lines:
    #Break apart line into words
    #Add code here

    
    #Process each word in the line
    for word in words:
        #if word is greater than 2 characters write to file
        #Add code here

        
    #go to next line by writing a newline character to your file
    #Add code here
        
#close the file
#Add code here

        

## regular.txt
## This is a test
## of reading files
## Jack be nimble
## Jack be quick
## Mary had a little lamb
## Whose fleece looked like a candlestick
## It was not fireproof
##
## shorter.txt       
## This test 
## reading files 
## Jack nimble 
## Jack quick 
## Mary had little lamb 
## Whose fleece looked like candlestick 
## was not fireproof
