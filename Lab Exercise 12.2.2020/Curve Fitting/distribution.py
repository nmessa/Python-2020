#Lab Exercise 11/13/2019
#Author: nmessa
## distribution.py
## Program to demonstrate 3 Probability Distribution Functions
## Author: nmessa

import pylab, random

def testErrors(ntrials=10000,npts=100):
    results = [0] * ntrials
    for i in range(ntrials):
        s = 0   # sum of random points
        for j in range(npts):
            s += random.triangular(-1,1)
        results[i] =s
    # plot results in a histogram
    pylab.hist(results,bins=50)
    pylab.title('Sum of 100 random points -- Triangular PDF (10,000 trials)')
    pylab.xlabel('Sum')
    pylab.ylabel('Number of trials')

def testErrors2(ntrials=10000,npts=100):
    results = [0] * ntrials
    for i in range(ntrials):
        s = 0   # sum of random points
        for j in range(npts):
            s += random.gauss(10,2)     #mean = 10 standard deviation = 2
        results[i] =s
    # plot results in a histogram
    pylab.hist(results,bins=50)
    pylab.title('Sum of 100 random points -- Gaussian PDF (10,000 trials)')
    pylab.xlabel('Sum')
    pylab.ylabel('Number of trials')

def testErrors3(ntrials=10000,npts=100):
    results = [0] * ntrials
    for i in range(ntrials):
        s = 0   # sum of random points
        for j in range(npts):
            s += random.uniform(1,100)     
        results[i] =s
    # plot results in a histogram
    pylab.hist(results,bins=50)
    pylab.title('Sum of 100 random points -- Uniform PDF (10,000 trials)')
    pylab.xlabel('Sum')
    pylab.ylabel('Number of trials')
    
testErrors()
pylab.show()
testErrors2()
pylab.show()
testErrors3()
pylab.show()
