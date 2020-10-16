from random import *

capitals={"Washington":"Olympia","Oregon":"Salem",\
                "California":"Sacramento","Ohio":"Columbus",\
                "Nebraska":"Lincoln","Colorado":"Denver",\
                "Michigan":"Lansing","Massachusetts":"Boston",\
                "Florida":"Tallahassee","Texas":"Austin",\
                "Oklahoma":"Oklahoma City","Hawaii":"Honolulu",\
                "Alaska":"Juneau","Utah":"Salt Lake City",\
                "New Mexico":"Santa Fe","North Dakota":"Bismarck",\
                "South Dakota":"Pierre","West Virginia":"Charleston",\
                "Virginia":"Richmond","New Jersey":"Trenton",\
                "Minnesota":"Saint Paul","Illinois":"Springfield",\
                "Indiana":"Indianapolis","Kentucky":"Frankfort",\
                "Tennessee":"Nashville","Georgia":"Atlanta",\
                "Alabama":"Montgomery","Mississippi":"Jackson",\
                "North Carolina":"Raleigh","South Carolina":"Columbia",\
                "Maine":"Augusta","Vermont":"Montpelier",\
                "New Hampshire":"Concord","Connecticut":"Hartford",\
                "Rhode Island":"Providence","Wyoming":"Cheyenne",\
                "Montana":"Helena","Kansas":"Topeka",\
                "Iowa":"Des Moines","Pennsylvania":"Harrisburg",\
                "Maryland":"Annapolis","Missouri":"Jefferson City",\
                "Arizona":"Phoenix","Nevada":"Carson City",\
                "New York":"Albany","Wisconsin":"Madison",\
                "Delaware":"Dover","Idaho":"Boise",\
                "Arkansas":"Little Rock","Louisiana":"Baton Rouge"}

#Pick a state at random and store it's capital
#This will pick a key at random by making a list of keys
correct = 0
numQuestions = 5
for i in range(numQuestions):
    pick = choice(list(capitals.keys()))
    capital = capitals[pick]
    del capitals[pick]

    #quiz
    print ("What is the capital of", pick, "? ", end ="")
    answer = input()

    #check for correct
    if answer == capital:
        print ("Correct")
        correct += 1
    else:
        print ("No, the capital of", pick, "is", capital)

print ("You got", correct, "out of", numQuestions, "correct")
        
                  


