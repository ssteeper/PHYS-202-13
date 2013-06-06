function [m, b, merror, berror] = WeightedLSQFit(x,y,w)
    %Take in arrays representing (x,y) values for a set of linearly varying data and an array of weights w.
    %perform a weighted linear least squares regression. Return the resulting slope and intercept
    %parameters of the best fit line with their uncertainties.
    %if the weights are all equal to one, the uncertainties on the parameters are calculated using the
    %non-weighted least squares equations.
    wsum = sum(w);

    wx = sum(w.*x);
    wxsq = sum(w.*x.^2);
    wy = sum(w.*y);
    wxy = sum(w.*x.*y);
    
    b = (wxsq.*wy-wx.*wxy)/(wsum.*wxsq-wx^2);
    m = (wsum.*wxy-wx*wy)/(wsum.*wxsq-wx^2);
    
    merror = (wsum/(wsum.*wxsq-wx^2))^.5;
    berror = (wxsq/(wsum.*wxsq-wx^2))^.5;

end

