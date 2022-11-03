# Could not find parametric but found the polar form for Fermat's Spiral: [https://mathworld.wolfram.com/FermatsSpiral.html]
# r^2 = a^2 * theta
# Converted from polar -> cartesian -> parametric to form for Fermat's:
# X = a * sqrt(theta) * cos(theta)
# Y = a * sqrt(theta) * sin(theta)

# Found the butterfly curve online in parametric form fortunately [https://mathworld.wolfram.com/ButterflyCurve.html]
# X = sin(theta)

import numpy as np
import matplotlib.pyplot as plot

from matplotlib import cm
from matplotlib.collections import LineCollection

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

def T1(): # Plot a circle
    X, Y = GenerateCircle(5, (4, 2))
    plot.plot(X, Y) 
    plot.axis("equal")

def T2(): # Fermat's Spiral Parametric
    X,Y, X2, Y2 = GenerateFermatsSpiral(5, 20)
    plot.plot(X, Y)
    plot.plot(X2, Y2)
    plot.axis("equal")

def T3(): # Butterfly Curve
    X, Y = GenerateButterflyCurve(1, 100)
    plot.plot(X, Y, c=(0.1, 0.2, 0.3)) 
    plot.axis("equal")

def GenerateAndDrawCircle(radius, centre):
    X,Y = GenerateCircle(radius, centre)
    plot.plot(X, Y)
    

def E1(): # Multiple Circles
    GenerateAndDrawCircle(1, (0,0))
    GenerateAndDrawCircle(2, (0,0))
    GenerateAndDrawCircle(3, (0,0))
    GenerateAndDrawCircle(4, (0,0))
    GenerateAndDrawCircle(5, (0,0))

    plot.axis("equal")

def E2(): # Colour changing with respect to X-Coordinate
    fig, axis = plot.subplots()
    
    axis.set_xlabel("X")
    axis.set_ylabel("Y")
    
    X,Y = GenerateButterflyCurve(1, 100)
    Points = []

    for i in range(0, len(X)-1): # there are N-1 lines 
        Points.append([(X[i],Y[i]), (X[i + 1], Y[i + 1])]) # creating edges between p0, p1 and p1, p2 ... p(n-1), pn
    
    collection = LineCollection(Points)
    collection.set_cmap("twilight")
    collection.set_array(Y) # set colour relative to X

    axis.add_collection(collection)
    axis.set_aspect("equal")
    axis.autoscale_view()

def E3(): # Colour becoming lighter with increasing radius 
    X1, Y1, X2, Y2 = GenerateFermatsSpiral(5, 20)

    fig, axis = plot.subplots()

    axis.set_xlabel("X")
    axis.set_ylabel("Y")

    Points1 = []
    Points2 = []

    R1 = np.sqrt(X1*X1 + Y1*Y1) # performing np.flip makes it darker with increasing radius and honestly, looks better
    R2 = np.sqrt(X2*X2 + Y2*Y2)

    for i in range(0, len(X1)-1):
        Points1.append([(X1[i], Y1[i]), (X1[i + 1], Y1[i + 1])])

    for i in range(0, len(X2)-1):
        Points2.append([(X2[i], Y2[i]), (X2[i + 1], Y2[i + 1])])

    Collection1 = LineCollection(Points1,cmap="twilight")
    Collection1.set_array(R1)

    Collection2 = LineCollection(Points2, cmap="twilight")
    Collection2.set_array(R2)

    axis.add_collection(Collection1)
    axis.add_collection(Collection2)

    axis.set_aspect("equal")
    axis.autoscale_view()

E3()

plot.show()
