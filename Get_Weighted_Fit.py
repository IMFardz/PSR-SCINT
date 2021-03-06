# Use this to get weighted fits

import numpy as np
import matplotlib.pyplot as plt
import astropy.units as u
import scipy.optimize as sc

def f(x, a, b):
    """A linear function"""
    return a*x + b

def scipy_weight(xdata, ydata, yerr, get_cov=True):
    """Return a weighted least square linear regression for the given set of values
    and y-errors"""
    fit, cov = sc.curve_fit(f, xdata = xdata, ydata = ydata, sigma=yerr)
    if get_cov:
        return fit, cov
    else:
        return fit
    


