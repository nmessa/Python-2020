## Lab Exercise 11/5/2020 Problem 2
## Author: 
## Silly sentence generator writing them to a file
## Files are stored in a text file with one element per line

from random import *

#open files and read to lists
#open adjectives.txt and read files to the list adjectives
myFile = open('adjectives.txt', 'r')
adjectives = myFile.readlines()
myFile.close()
#strip off newline characters
for i in range(len(adjectives)):
    adjectives[i] = adjectives[i].rstrip()
     
#open nouns.txt and read files to the list nouns
#Add code here
    


#open adverbPhrases.txt and read files to the list adverbPhrses
#Add code here

    

#open verbPhrases.txt and read files to the list verbPhrses
#Add code here

    

#Create the sentence
#Add code here

    

#Print the sentence
print (sentence)



