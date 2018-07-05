# This script gets the error bars for the individual points when measuring the differential scintillation
import numpy as np

def ipartial(real, imaginary):
    return (1/(real*(1 + (imaginary/real)**2)))**2

def rpartial(real, imaginary):
    return (1/(real**2*(1 +(imaginary/real)**2)))**2

def GetPlot(cross, xlim):
    """Return the plot  errorbars for the associated points as a one-dimensional numpy array

    Cross: The cross secondary spectrum, already binned. First dimension assumed to be 
    doppler frequency, second dimension is time delay. Only positive time delays should be
    plotted.
    """
    
    copy, domain  = RemoveNans(cross, xlim)
    mean = np.nanmean(copy, axis=0)
    real = np.real(mean)
    imaginary = np.imag(mean)
    realstd = np.nanstd(np.real(copy), axis=0)/np.sqrt(copy.shape[0])
    imagstd = np.nanstd(np.imag(copy), axis=0)/np.sqrt(copy.shape[0])
    std = np.sqrt(ipartial(real,imaginary)*(np.abs(imagstd))**2 + \
                      rpartial(real,imaginary)*(np.abs(realstd))**2)
    
    return domain, np.angle(mean), std

def RemoveNans(cross, xlim=None):
    """Remove vertical axis whose values are all nan and return new matrix"""
    temp = np.argwhere(np.isnan(cross[-1,:]))[:,0]
    nans = np.array([])
    for nan in temp:
        if (np.isnan(cross[:,nan])).all():
            nans = np.append(nans, nan)
    copy = np.delete(cross, nans, axis=1)
    length = cross.shape[1]//2
    if xlim is not None:
        domain = np.arange(-length, length) + 0.5
        domain *= (xlim/domain[-1])
        domain = np.delete(domain, nans)
        return copy, domain
    else:
        return copy
    
    
    
