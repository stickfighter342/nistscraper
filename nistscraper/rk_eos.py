# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 11:17:16 2020

@author: 21EthanD
"""
from scipy.optimize import fsolve
import numpy as np
r = 0.0821 #atm * L / mol / K

def eos(p, t, v):
    """
    y = data[0]
    t = y[0]
    v = y[1]"""
    tc = 126.2
    pc = 33.5    
    a = 0.42748 * r * r * pow(tc, 2.5) / pc
    b = 0.08664 * r * tc / pc
    return p + a / (pow(t, 0.5) * v * (v + b)) - r * t / (v - b)


a = fsolve(eos, 0, args=(200,));
print(a)


def errorIdeal(rk, igl):
    return abs(rk - igl) * 100
