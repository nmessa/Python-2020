#Lab Exercise 11/13/2019
#Author: nmessa
#spring3.py
#This will plot data of amount a spring is stretched with a
#with a given amount of mass (Force) applied
#The program will use the polyfit function to find the line the linear and
#cubic fits for the data
import pylab

def getData(fileName):
    dataFile = open(fileName, 'r')
    distances = []
    masses = []
    discardHeader = dataFile.readline() #remove header from the file

    #read in each line of the data file and break it up into distance and mass
    for line in dataFile:
        d, m = line.split()
        #add distances and mass to lists
        distances.append(float(d))
        masses.append(float(m))
    dataFile.close()
    return (masses, distances)

def fitData2(fileName):
    xVals, yVals = getData(fileName)
    xVals = pylab.array(xVals)
    yVals = pylab.array(yVals)
    xVals = xVals*9.81  # convert mass to force (F = mg)
    pylab.plot(xVals, yVals, 'bo', label = 'Measured displacements')
    pylab.title('Measured Displacement of Spring')
    pylab.xlabel('Force (Newtons)')
    pylab.ylabel('Distance (meters)')
    a,b = pylab.polyfit(xVals, yVals, 1)
    #equation for order 1 curve
    estYVals = a*xVals + b
    pylab.plot(xVals, estYVals, label = 'Linear fit')
    a,b,c,d = pylab.polyfit(xVals, yVals, 3)
    #equation for order 3 curve
    estYVals = a*(xVals**3) + b*xVals**2 + c*xVals + d
    pylab.plot(xVals, estYVals, label = 'Cubic fit')
    pylab.legend(loc = 'best')

fitData2('springData.txt')
pylab.show()
