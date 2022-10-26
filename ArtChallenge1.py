# Could not find parametric but found the polar form for Fermat's Spiral: [https://mathworld.wolfram.com/FermatsSpiral.html]
# r^2 = a^2 * theta
# Converted from polar -> cartesian -> parametric to form for Fermat's:
# X = a * sqrt(theta) * cos(theta)
# Y = a * sqrt(theta) * sin(theta)

# Found the butterfly curve online in parametric form fortunately [https://mathworld.wolfram.com/ButterflyCurve.html]
# X = sin(theta)

import numpy as np
import matplotlib.pyplot as plot

def GenerateCircle(radius, centre):
    t = np.arange(0, (np.pi * 2) + 0.1, 0.1) # 2pi is full circle, the + 0.1 is bc range is a weird function where it's non-inclusive 

    XPoints = centre[0] + (np.cos(t) * radius)
    YPoints = centre[1] + (np.sin(t) * radius)

    return XPoints, YPoints

def GeneratePositiveFermatsSpiral(a, nSpirals): # polar coord: r^2 = a^2 * theta
    t = np.arange(0, (np.pi * 2 * nSpirals) + 0.1, 0.1)
    
    XPoints = a * np.sqrt(t) * np.cos(t)
    YPoints = a * np.sqrt(t) * np.sin(t)

    return XPoints, YPoints

def GenerateFermatsSpiral(a, nSpirals): # a represents size 
    t = np.arange(0, (np.pi * 2 * nSpirals) + 0.1, 0.1)
    
    XPoints1 = a * np.sqrt(t) * np.cos(t)
    YPoints1 = a * np.sqrt(t) * np.sin(t)

    XPoints2 = (-1) * XPoints1 # for the negative part of the square root
    YPoints2 = (-1) * YPoints1

    return XPoints1, YPoints1, XPoints2, YPoints2

def GenerateButterflyCurve(size, thickness):
    t = np.arange(0, (np.pi * thickness) + 0.1, 0.01)

    XPoints = size * np.sin(t) * (np.e**np.cos(t) - (2 * np.cos(4 * t)) + np.sin((1/12) * t)**5)
    YPoints = size * np.cos(t) * (np.e**np.cos(t) - (2 * np.cos(4 * t)) + np.sin((1/12) * t)**5)

    return XPoints, YPoints

def GenerateSin():  
    XPoints = np.arange(0, 3 * np.pi, 0.1)
    YPoints = np.sin(XPoints)

    return XPoints, YPoints

# T1 (Plot a circle)
#X, Y = GenerateCircle(5, (4, 2))
# T2 (Fermat's Spiral Parametric)
#X,Y, X2, Y2 = GenerateFermatsSpiral(5, 20)
# T3 (Butterfly Curve)
X, Y = GenerateButterflyCurve(1, 100)

plot.axis("equal")

plot.plot(X, Y)
#plot.plot(X2, Y2) # for Fermat's spiral (T2, E3)

plot.show()
