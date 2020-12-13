## Lab Exercise 12/17/2020 Pin Cipher
## Author: 
## This is a Julius Ceasar cipher for PIN numbers

def PINCipher(pin, shift):
    cipherText = ""
    #Add code here
    
    return cipherText   

#Test code
pin = '12345'
shift = 1
print (PINCipher(pin, shift)) #23456
shift = 6
print (PINCipher(pin, shift)) #78901
shift = 23
print (PINCipher(pin, shift)) #45678
shift = -1
print (PINCipher(pin, shift)) #01234
