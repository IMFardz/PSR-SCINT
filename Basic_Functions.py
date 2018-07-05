()# This script contains some basic methods to shorten code

import numpy as np

def rebin(cross, xshape, yshape):
    """Rebins a 2-Dimensional array into an array with shape (xshape, yshape)"""
    copy = cross.reshape(cross.shape[0], yshape, cross.shape[1]//yshape).mean(axis=2)
    copy = copy.reshape(xshape, copy.shape[0]//xshape, copy.shape[1]).mean(axis=1)
    return copy

def get_gate(profile, minphase, maxphase, scale=True, flip_axis=True):
    """Given a three dimensional pulse profile, returns a two dimensional dynamic sectrum"""
    total_phase_bins = profile.shape[-1]
    gate = profile[:,:,minphase:maxphase].mean(axis=-1)
    if scale:
        gate *=(total_phase_bins/(maxphase-minphase))
    if flip_axis:
        gate = gate.T
    
    return gate

def get_on_gate(profile, min_on, max_on, min_off, max_off):
    """Returns the scaled on gate"""
    on = get_gate(profile, min_on, max_on)
    off = get_gate(profile, min_off, max_off)
    gate = on/off - 1
    return gate


