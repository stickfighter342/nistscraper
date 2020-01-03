# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 10:50:01 2020

@author: 21EthanD
"""
import numpy as np
import matplotlib.pyplot as plt

def ideal_gas_law(T, Vm):
    """Calculates the pressure in atm of a gas given the temperature in K and the molar volume in L/mol using the ideal gas law
    """
    R = 0.08205 #L*atm/K/mol
    return R * T / Vm


