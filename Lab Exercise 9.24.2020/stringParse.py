##Parsing a string demo
##Author: nmessa
##Date: 9/11/2019

testString = "I've been from Tucson to Tucumcari, Tehachapi to Tonapah"
vowels = "AEIOUaeiou"
count = 0
count2 = 0

#use for counting loop to parse the string
for i in range(len(testString)):
    if testString[i] in vowels:
        count += 1
print("There are", count, "vowels in the test string")

for letter in testString:
    if letter in vowels:
        count2 += 1
print("There are", count2, "vowels in the test string")
    
##Output
##There are 20 vowels in the test string
##There are 20 vowels in the test string
