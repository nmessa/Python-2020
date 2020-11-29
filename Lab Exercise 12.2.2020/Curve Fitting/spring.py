#Lab Exercise 11.13.2019
#Author: nmessa
#spring.py
#This will plot data of amount a spring is stretched with a
#with a given amount of mass (Force) applied
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

def plotData(fileName):
    xVals, yVals = getData(fileName)
    xVals = pylab.array(xVals)
    yVals = pylab.array(yVals)
    xVals = xVals*9.81 # convert mass to force (F = mg)
    pylab.plot(xVals, yVals, 'bo', label = 'Measured displacements')
    pylab.title('Measured Displacement of Spring')
    pylab.xlabel('Force (Newtons)')
    pylab.ylabel('Distance (meters)')

plotData('springData.txt')
pylab.show()
