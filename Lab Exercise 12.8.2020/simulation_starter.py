#simulation_starter.py
#Author: 
#Lab Exercise 12.8.2020
#Improved version that runs a simulation of three trials of one million coin flips
#one million dice rolls and one million roulette wheel spins

import random
rollTally = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
flipTally = {'H':0, 'T':0}
rollTotal = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
flipTotal = {'H':0, 'T':0}
#Add code for rouletteTally and rouletteTotal dictionaries

def flipCoin():
    '''
    This models a flip of a fair coin
    '''
    #ADD CODE HERE

def rollDice():
    '''
    This models the roll of two fair die
    '''
    #ADD CODE HERE

def spinWheel():
    '''
    This models the spin of a roulette wheel
    '''
    #ADD CODE HERE

    

def flipSim(n):
    '''
    This simulates the flip of a coin n times
    '''
    #ADD CODE HERE

def rollSim(n):
    '''
    This simulates the roll of two die n times
    '''
    #ADD CODE HERE

def spinSim(n):
    '''
    This simulates the spin of a roulette wheel n times
    '''
    #ADD CODE HERE


    
def calcMean(X):
    '''
    This returns the arithmetic mean of any numeric list
    '''
    #ADD CODE HERE

def stdDev(X):
    '''
    This returns the standard deviation of any numeric list
    '''
    mean = calcMean(X)
    total = 0.0
    for x in X:
        tot += (x - mean)**2
    return (total/len(X))**0.5

def printHistogram(X):
    '''
    This will print a histogram of a dictionary containing numeric values
    '''
    #test = ('H', 'T')
    print()
    print ("Histogram")
    keyList = list(X.keys())                          #get a list of keys in the dictionary
    maxValue = 0
    for e in keyList:                               #find the maximum value of data in the dictionary
        if X[e] > maxValue:
            maxValue = X[e]
    scaleFactor = 40.0 / maxValue       #determine the scale factor based on data to ensure
                                                             #Histogram fits on screen
    for e in keyList:                               #scale the data
        X[e] *= scaleFactor
    for e in keyList:                               #typecast the data to an integer value
        X[e] = int(X[e])
    vals = list(X.values())                               #make a list of the values in the dictionary
    for i in range(len(vals)):                  #print the histogram
        if keyList[i] not in test:
            if keyList[i] < 10:
                print (keyList[i], " ",end = '')
            else:
                print (keyList[i], "",end = '')
        else:
            print (keyList[i], "",end = '')
                
        for i in range(vals[i]):
            print ("X",end = '')
        print()
    print()
    print()

        
def  runSimulation(function, n, numTrials, simDict , totalDict):
    for trial in range(1, numTrials+1):
        dict = simDict.copy()               #reset the dictionary counts to 0
        print ("Trial", trial)
        answer = function(n)                #roll or flip n times
        for e in answer:
            dict[e] += 1                           #add up the values for each outcome
        print (dict)
        keyList = list(dict.keys())
        for e in keyList:
            totalDict[e] += dict[e]         #add values to totalDict
    print()
    #Calculate average of numTrials trials
    for e in keyList:
        totalDict[e] /= float(numTrials)
    #Round the values in the dictionary
    for e in keyList:
        totalDict[e] = round(totalDict[e], 2)
    #Print the rounded average
    print ("Average = ", totalDict)
    printHistogram(totalDict)

#simulate a million flip coin toss done 3 times
print ("Running Coin Flip Simulation ....")
runSimulation(flipSim, 1000000, 3, flipTally, flipTotal)

#simulate a million roll dice roll done 3 times
print ("Running Dice Roll Simulation ....")
runSimulation(rollSim, 1000000, 3, rollTally, rollTotal)

#simulate a million spins of a roulette done 3 times
print ("Running Roulette Wheel Simulation ....")
runSimulation(spinSim, 1000000, 3, rouletteTally, rouletteTotal)      
    
        
    
