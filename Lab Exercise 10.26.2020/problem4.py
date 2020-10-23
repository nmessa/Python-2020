## Lab Exercise 10/26/2020 Problem 4
## Author: 
## This program will validate a password

#This function will test a password for adequate security
def isValid(password):
    #initialize counters to 0
    #Add code here
    
    
    #check for length
    #Add code here

    

    #Check each character for uppercase, lowercase, and digit characters
    #Add code here
    

    #if correct number of uppercase, lowercase, and digit characters
    #return True or else return False
    #Add code here

    

#test code for isValid function
##print isValid('test') #False - too short
##print isValid('abcdefgh') #False no upper case no digit
##print isValid('abcDefgh') #False no digit
##print isValid('ab2defgh') #False no upper case
##print isValid('abCde3gh') #True

#Print user instructions
print("Enter your password twice")
print('Your password must contain at least 8 characters')
print('It must contain at least 1 upper case, 1 lower case, and 1 digit')


#set flag variable valid to false
#Add code here



#Test the password algorithm
#Add code here



##Sample Output
##Enter your password twice
##Your password must contain at least 8 characters
##It must contain at least 1 upper case, 1 lower case, and 1 digit
##Enter a password: abcDefgh5
##Enter your password again: abcDefgh5
##Valid password
