#Lab Exercise 11/13/2019
#Author: nmessa
#spring5.py
#This will plot data of amount a spring is stretched with a
#with a given amount of mass (Force) applied
#The program will use the polyfit function to find the linear and cubic fits
#of the data I have removed 5 data points from the end of the data to see if
#it looks like with a linear fit
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

def fitData5(fileName):
    xVals, yVals = getData(fileName)
    #remove the last 5 elements of the data set
    xVals = pylab.array(xVals[:-6])
    yVals = pylab.array(yVals[:-6])
    xVals = xVals*9.81  # convert mass to force (F = mg)
    pylab.plot(xVals, yVals, 'bo', label = 'Measured points')
    pylab.title('Measured Displacement of Spring')
    pylab.xlabel('Force (Newtons)')
    pylab.ylabel('Distance (meters)')
    a,b = pylab.polyfit(xVals, yVals, 1)  # fix y = ax + b
    # use line equation to graph predicted values
    estYVals = a*xVals + b
    k = 1/a
    pylab.plot(xVals, estYVals, label = 'Linear fit, k = '
               + str(round(k, 5)))
    pylab.legend(loc = 'best')

fitData5('springData.txt')
pylab.show()
