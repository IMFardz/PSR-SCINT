# Use this script for getting the cross secondary spectrum
import numpy as np


def get_cross(spec1, spec2):
    """Computes and returns the cross secondary spectrum"""
    spec1 = np.fft.fft2(spec1)
    spec2 = np.fft.fft2(spec2)
    spec1 = np.fft.fftshift(spec1)
    spec2 = np.fft.fftshift(spec2)
    cross = spec1 * np.conj(spec2)
    return cross


def get_axis_lims(xlen, ylen, tmin, tmax, fmin, fmax):
    """Returns the x and y limits after computing the Fourier Transform"""
    xlim = (xlen/(tmax-tmin))/2
    ylim = (ylen/(fmax-fmin))/2
    return xlim, ylim
    

def remove_leakages(cross, xmin, xmax, ymin, ymax):
    """Removes the indices between xmin and xmas and ymin and ymax"""
    cross[:,ymin:ymax] = np.nan
    cross[xmin:xmax,:] = np.nan
    return cross
