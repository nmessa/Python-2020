import math

def sphereArea(r):
    '''
    Computes the surface area of a sphere of given radius. Returns that
    value as a float.
    r: radius - float
    returns: float
    '''
    answer = 4 * math.pi * r**2
    return answer

def sphereVolume(r):
    '''
    Computes the volume of a sphere of given radius. Returns that
    value as a float.
    r: radius - float
    returns: float
    '''
    answer = 4.0/3.0 * math.pi * r**3
    return answer

def evaluatePoly(poly, x):
    '''
    Computes the value of a polynomial function at given value x. Returns that
    value as a float.
    poly: list of numbers, length > 0
    x: number
    returns: float
    '''
    value = 0.0
    for i in range(len(poly)):
        value += poly[i] * x**i
    return value

def computeDeriv(poly):
    '''
    Computes and returns the derivative of a polynomial function as a list of
    floats. If the derivative is 0, returns [0.0].
 
    poly: list of numbers, length &gt; 0
    returns: list of numbers (floats)
    '''
    deriv = []
    for i in range(1, len(poly)):
        temp = float(poly[i] * i)
        deriv.append(temp)
    if len(deriv) == 0:
        return [0.0]
    else:
        return deriv

def computeRoot(poly, x_0, epsilon):
    '''
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a list containing the root and the number of iterations required
    to get to the root.
 
    poly: list of numbers, length > 1.
         Represents a polynomial function containing at least one real root.
         The derivative of this polynomial function at x_0 is not 0.
    x_0: float
    epsilon: float > 0
    returns: list [float, int]
    '''
    root = x_0
    iterations = 0
    
    while abs(evaluatePoly(poly, root))> epsilon:
        root = root - evaluatePoly(poly, root)/evaluatePoly(computeDeriv(poly), root)
        iterations += 1
    result = []
    result.append(root)
    result.append(iterations)
    return result

def cuboidArea(l, w, h):
    '''
    Computes the surface area of a cuboid with a given length (r), width (w) and height (h). Returns that
    value as a float.
    l: length is either an int or float
    w: width is either an int or float
    h: height is either an int or float
    returns: float
    '''
    answer = 2 * l * w + 2 * l * h + 2 * w * h
    return answer

def cuboidVolume(l, w, h):
    '''
    Computes the volume of a cuboid with a given length (r), width (w) and height (h). Returns that
    value as a float.
    l: length is either an int or float
    w: width is either an int or float
    h: height is either an int or float
    returns: float
    '''
    answer = l * w * h
    return answer

def polyPrettyPrint(poly):
    '''
    Builds a string of a polynomial function that is more readable than a list of numbers.
    poly: list of numbers, length > 0
    returns: string
    '''
    result = ''
    for i in range(len(poly)-1, -1, -1):
        if poly[i] < 0 or i == len(poly)-1:
            result += " " + str(poly[i]) + "X^" + str(i)
        else:
            result += " + " + str(poly[i]) + "X^" + str(i)
    return result



            
