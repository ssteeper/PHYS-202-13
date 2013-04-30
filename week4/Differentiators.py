import numpy as np
def finiteDifference(x,y):
    """takes two arrays, x and y, and returns the derivative of y with respect to x, dydx"""
    dydx = np.zeros(y.shape,float)
    dydx[:-1] = diff(y)/diff(x)
    dydx[-1] = (y[-1] - y[-2])/(x[-1] - x[-2])
    return dydx

def fourPtFiniteDiff(x,y):
    dydx= np.zeros(y.shape, float)
    h=x[1]-x[0]
    dydx[2:-2] = (y[-2] - 8*y[-1] + 8*y[1] - y[2])/12*h
    return dydx
