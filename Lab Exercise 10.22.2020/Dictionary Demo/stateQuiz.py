

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

done = False
while not done:
    state = input('Enter the name of the state: ')
    print ("The capital of", state, "is", capitals[state])
    answer = input("Another state? (y/n) ")
    if answer != 'y':
        done = True
        print ('Bye, bye!!!')
        
                  


