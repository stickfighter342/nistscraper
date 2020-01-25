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


def cTOall(value, key):
    if (key == "temp"):  
        return [value, value * 1.8 + 32, value + 273.15, (value + 273.15) * 1.8]
    elif (key == "pres"):
        return [value, value * 101.325, value * 1.01325, value * 14.6959]
    

def arrTemp(initial, temp):
    if (initial == "r"):
        temp = (temp - 491.67) / 1.8
    elif (initial == "k"):
        temp -= 273.15
    elif (initial == "f"):
        temp = (temp - 32) / 1.8
    return cTOall(temp, "temp")    


def convTemp(initial, temp, convert):
    vec = arrTemp(initial, temp)
    if (convert == "r"):
        return vec[3]
    elif (convert == "k"):
        return vec[2]
    elif (convert == "f"):
        return vec[1]
    return vec[0]

def arrPres(initial, pres):
    if (initial == "psi"):
        pres /= 14.6959
    elif (initial == "kPa"):
        pres /= 101.325
    elif (initial == "bar"):
        pres /= 1.01325
    return cTOall(pres, "pres")  
    
def convPres(initial, pres, convert):
    vec = arrPres(initial, pres)
    if (convert == "psi"):
        return vec[3]
    elif (convert == "bar"):
        return vec[2]
    elif (convert == "kPa"):
        return vec[1]
    return vec[0]

def convVol(initial, vol, convert):
    if (initial == "L/mol"):
        return vol * 0.001
    return vol * 1000
