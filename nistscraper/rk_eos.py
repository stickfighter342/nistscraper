# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 11:17:16 2020

@author: 21EthanD

Contains residual functions for several equations of state.
Currently limited to RK EOS.
"""
from scipy.optimize import fsolve
import numpy as np

Rgas = 0.0821 #atm * L / mol / K

def eos(P, T, v):
    """
    Returns the residual of the Redlich-Kwong equation of state.
    
    Parameters
    ----------
    P: Pressure in atm (int or list-like object)
    
    Returns
    -------
    res:
    
    Examples
    --------
    
    y = data[0]
    t = y[0]
    v = y[1]"""
    Tc = 126.2
    Pc = 33.5    
    a = 0.42748*Rgas**2*Tc**2.5/Pc
    b = 0.08664*Rgas*Tc/Pc
    res = P + a/(T**0.5*v*(v + b)) - Rgas *T/(v - b)
    return res


a = fsolve(eos, 0, args=(200, 300));
print(a)


def errorIdeal(rk, igl):
    return abs(rk - igl) * 100
