def LinearLeastSquaresFit(x,y):
    "Take in arrays representing (x,y) values for a set of linearly varying data and perform a linear least squares regression. Return the resulting slope and intercept parameters of the best fit line with their uncertainties."""
    n = float(len(x))
    X = sum(x)/n
    Y = sum(y)/n
    X2 = sum(x**2)/n
    XY = sum(x*y)/n
    
    slope = (XY - X*Y) / (X2 - X**2)
    intercept = (X2*Y - X*XY) / (X2 - X**2)
    D = y - (slope*x + intercept)
    D2 = sum(D**2)/n
    
    slerr = ((1/(n-2))*(D2/(X2 - (X**2))))**.5
    interr = ((1/(n-2))*((D2*X2)/(X2 - (X**2))))**.5
    return slope, intercept, slerr, interr

def WeightedLinearLeastSquaresFit(x,y,w):
    """Take in arrays representing (x,y) values for a set of linearly varying data and an array of weights w.
    perform a weighted linear least squares regression. Return the resulting slope and intercept
    parameters of the best fit line with their uncertainties.
    if the weights are all equal to one, the uncertainties on the parameters are calculated using the
    non-weighted least squares equations."""
    wsum = sum(w)
    weightless=True
    for i in w:
        if i!=1:
            weightless=False
    if weightless:
        return LinearLeastSquaresFit(x,y)
    
    wx = sum(w*x)
    wxsq = sum(w*x**2)
    wy = sum(w*y)
    wxy = sum(w*x*y)
    b = (wxsq*wy-wx*wxy)/(wsum*wxsq-wx**2)
    m = (wsum*wxy-wx*wy)/(wsum*wxsq-wx**2)
    
    merror = (wsum/(wsum*wxsq-wx**2))**.5
    berror = (wxsq/(wsum*wxsq-wx**2))**.5
    return m,b,merror,berror
