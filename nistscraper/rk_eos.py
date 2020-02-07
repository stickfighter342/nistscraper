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
    P: Pressure in atm (double or list-like object)
    T: Temperature in Kelvin (a constant - double or int)
    v: Volume in liters (a constant - double or int)
        
    Returns
    -------
    double
        residual of Redlich-Kwong equation of state
    
    Examples
    --------
    P = 3.0 atm
    T = 273.15 K
    v = 10 L
    Input: eos(3, 273.15, 10) 
    Output: 0.7606994048189883
    
    
    """
    Tc = 126.2
    Pc = 33.5    
    a = 0.42748*Rgas**2*Tc**2.5/Pc
    b = 0.08664*Rgas*Tc/Pc
    res = P + a/(T**0.5*v*(v + b)) - Rgas *T/(v - b)
    return res


a = fsolve(eos, 0, args=(273.15, 4));
print(eos(3, 273.15, 10))


def errorIdeal(rk, igl):
    return abs(rk - igl) * 100
