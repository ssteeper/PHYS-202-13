from math import *

def pointPotential(x, y, q, posx, posy):
    """Computes electric potential from charge q at posx, posy and returns the potential at x,y"""
    k = 8.98755178e9 
    return (k*q)/((x-posx)**2 + (y-posy)**2)**(.5)

def quadrupolePotential(x,y,q,d):
    """Computes potential at x,y in a quadrupole system with charges at +d and -d along the x and y axis"""
    return pointPotential(x,y,q,-d,0) + pointPotential(x,y,q,d,0) + pointPotential(x,y,q,0,-d) + pointPotential(x,y,q,0,d)
