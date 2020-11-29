#Lab Exercise 11/13/2019
#Author: nmessa
#spring4.py
#This will plot data of amount a spring is stretched with a
#with a given amount of mass (Force) applied
#The program will use the polyfit function to find the linear and cubic fits
#of the data I have added 5 data points to the end of the data to see if it
#looks like the cubic fit might be good
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

def fitData4(fileName):
    xVals, yVals = getData(fileName)
    #add 5 data elements to the data
    extX = pylab.array(xVals + [1.05, 1.1, 1.15, 1.2, 1.25])
    xVals = pylab.array(xVals)
    yVals = pylab.array(yVals)
    xVals = xVals*9.81  # convert mass to force (F = mg)
    extX = extX*9.81    # convert mass to force (F = mg)
    pylab.plot(xVals, yVals, 'bo', label = 'Measured displacements')
    pylab.title('Measured Displacement of Spring')
    pylab.xlabel('Force (Newtons)')
    pylab.ylabel('Distance (meters)')
    a,b = pylab.polyfit(xVals, yVals, 1)
    estYVals = a*extX + b
    pylab.plot(extX, estYVals, label = 'Linear fit')
    a,b,c,d = pylab.polyfit(xVals, yVals, 3)
    estYVals = a*(extX**3) + b*extX**2 + c*extX + d
    pylab.plot(extX, estYVals, label = 'Cubic fit')
    pylab.legend(loc = 'best')

fitData4('springData.txt')
pylab.show()
