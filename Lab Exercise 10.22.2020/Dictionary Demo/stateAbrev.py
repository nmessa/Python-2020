## Dictionary Demo
## Author: nmessa
## Date: 10.14.2016

states={"WA":"Washington","OR":"Oregon",\
        "CA":"California","OH":"Ohio",\
        "NE":"Nebraska","CO":"Colorado",\
        "MI":"Michigan","MA":"Massachusetts",\
        "FL":"Florida","TX":"Texas",\
        "OK":"Oklahoma","HI":"Hawaii",\
        "AK":"Alaska","UT":"Utah",\
        "NM":"New Mexico","ND":"North Dakota",\
        "SD":"South Dakota","WV":"West Virginia",\
        "VA":"Virginia","NJ":"New Jersey",\
        "MN":"Minnesota","IL":"Illinois",\
        "IN":"Indiana","KY":"Kentucky",\
        "TN":"Tennessee","GA":"Georgia",\
        "AL":"Alabama","MS":"Mississippi",\
        "NC":"North Carolina","SC":"South Carolina",\
        "ME":"Maine","VT":"Vermont",\
        "NH":"New Hampshire","CT":"Connecticut",\
        "RI":"Rhode Island","RI":"Wyoming",\
        "MT":"Montana","KS":"Kansas",\
        "IA":"Iowa","PA":"Pennsylvania",\
        "MD":"Maryland","MO":"Missouri",\
        "AZ":"Arizona","NV":"Nevada",\
        "NY":"New York","WI":"Wisconsin",\
        "DE":"Delaware","ID":"Idaho",\
        "AK":"Arkansas","LA":"Louisiana"}

done = False
while not done:
    abrev = input('Enter the abbreviation of the state: ').upper()
    print ("The name of the state is ", states[abrev])
    answer = input("Another state? (y/n) ")
    if answer != 'y':
        done = True
        print ('Bye, bye!!!')
        
                  


