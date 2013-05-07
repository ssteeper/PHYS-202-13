

def pointPotential(x, y, q, posx, posy):
    """Computes electric potential from charge q at posx, posy and returns the potential at x,y"""
    k = 8.98755178e9 
    return (k*q)/((x-posx)**2 + (y-posy)**2)**(.5)

def quadrupolePotential(x,y,q,d):
    """Computes potential at x,y in a quadrupole system with charges at +d and -d along the x and y axis"""
    return pointPotential(x,y,q,-d,0) + pointPotential(x,y,q,d,0) + pointPotential(x,y,q,0,-d) + pointPotential(x,y,q,0,d)

def dipolePotential(x,y,q,d):
    """Computes potential at x,y in a dipole system with charges at +d and -d along the x axis"""
    return pointPotential(x,y,q,0,-d) - pointPotential(x,y,q,0,d) 

def pointField(x,y,q,Xq,Yq):
    """Computes electric field components (Ex, Ey) for position (x,y) from a charge q at (Xq, Yq)."""
    k = 8.98755178e9
    Ex = k*q*(x-Xq) / (((x-Xq)**2.0+(y-Yq)**2.0)**(.5))
    Ey = k*q*(y-Yq) / (((x-Xq)**2.0+(y-Yq)**2.0)**(.5))
    return (Ex, Ey)
