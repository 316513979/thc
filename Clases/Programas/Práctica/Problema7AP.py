import numpy
import math

def H_eps(x):
    e=0.01
    float(e)
    float(x)
    pi= numpy.pi
    if x<-e:
        return 0
    elif -e <= x and x <= e:
        H = 0.5 + (x/(2.0*e)) + (1/(2.0*e))*(math.sin((pi*x)/e))
        return H
    else:
        return 1
