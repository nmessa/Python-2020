## Lab Exercise 11/10/2020 Problem 4
## Author: 
## This displays a monetary amount in words
## Works up to $9999.99

#create dictionaries
money1000 = {0:'', 1:'One thousand ', 2:'Two thousand ', 3:'Three thousand ',
             4:'Four thousand ', 5:'Five thousand ', 6:'Six thousand ',
             7:'Seven thousand ', 8:'Eight thousand ', 9:'Nine thousand '}
money100 = {0:'', 1:'One hundred ', 2:'Two hundred ', 3:'Three hundred ',
             4:'Four hundred ', 5:'Five hundred ', 6:'Six hundred ',
             7:'Seven hundred ', 8:'Eight hundred ', 9:'Nine hundred '}
money10 = {0:'', 2:'Twenty ', 3:'Thirty ',4:'Forty ', 5:'Fifty ', 6:'Sixty ',
             7:'Seventy ', 8:'Eighty ', 9:'Ninety '}
money1 = {0:'', 1:'One ', 2:'Two ', 3:'Three ', 4:'Four ', 5:'Five ', 6:'Six ',
             7:'Seven ', 8:'Eight ', 9:'Nine '}
moneyTeens = {10:'Ten ', 11:'Eleven ', 12:'Twelve ', 13:'Thirteen ',
              14:'Fourteen', 15:'Fifteen ',16:'Sixteen ', 17:'Seventeen ',
              18:'Eighteen ', 19:'Nineteen '}
cents10 = {0:'', 2:'Twenty ', 3:'Thirty ',4:'Forty ', 5:'Fifty ', 6:'Sixty ',
             7:'Seventy ', 8:'Eighty ', 9:'Ninety '}
cents1 = {0:'', 1:'One ', 2:'Two ', 3:'Three ', 4:'Four ', 5:'Five ', 6:'Six ',
             7:'Seven ', 8:'Eight ', 9:'Nine '}
centsTeens = {10:'Ten ', 11:'Eleven ', 12:'Twelve ', 13:'Thirteen ',
              14:'Fourteen', 15:'Fifteen ',16:'Sixteen ', 17:'Seventeen ',
              18:'Eighteen ', 19:'Nineteen '}

#get monetary amount from user
#Add code here



#calculate number of dollars and number of cents
#Add code here



#break apart dollars digit by digit
#Add code here



#break apart cents digit by digit
#Add code here



#Build the dollars strings
#Add code here



#Build the cents strings
#Add code here



#print out the complete dollars and cents
print (m4 + m3 + m2 + m1 + 'dollars and ' + c2 + c1 + 'cents')

##Sample output
##Enter the monetary amount: $3452.74
##Three thousand Four hundred Fifty Two dollars and Seventy Four cents


