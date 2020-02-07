# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 10:50:01 2020

@author: 21EthanD
"""
import numpy as np
import matplotlib.pyplot as plt

def ideal_gas_law(T, Vm):
    """
    Calculates the pressure in atm of a gas given the temperature in K and the molar volume in L/mol using the ideal gas law
    
    Parameters
    ----------
    T: Temperature in Kelvin (a constant - double or int)
    Vm: Molar Volume (a constant - double or int)
    
    Returns
    -------
    double
        pressure of an ideal gas in atm according to the ideal gas law (given the temperature and the molar volume)
    
    Examples
    --------
    T = 298.15 K
    v = 2.0 L/mol
    Input: ideal_gas_law(298.15, 2.0)
    Output: 12.231603749999998 

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
    """
    Converts a temperature in given units to another temperature in specified units.
    Compatible units are Rankine, Kelvin, Fahrenheit, Celsius.
    
    
    Parameters
    ----------
    initial: numerical value of temperature to be converted (double or int)
    temp: units of initial temperature (specific string - "r" for Rankine, "k" for Kelvin, "f" for Fahrenheit, "c" for Celsius)
    convert: desired units of temperature to be converted (specific string - "r" for Rankine, "k" for Kelvin, "f" for Fahrenheit, "c" for Celsius)
    
    Returns
    -------
    double
        converted value of temperature in given desired units of temperature (Rankine, Kelvin, Fahrenheit, or Celsius)
    
    Examples
    --------
    initial = 0.0
    temp = "c"
    convert = "k"
    Input: convTemp(initial, temp, convert)
    Output: 273.15

    """
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
    """
    Converts a pressure in given units to another pressure in specified units.
    Compatible units are atmospheres, pounds per square inch, kilopascals, bar.
    
    
    Parameters
    ----------
    initial: numerical value of pressure to be converted (double or int)
    pres: units of initial pressure (specific string - "atm" for atmospheres, "psi" for pounds per square inch, "kPa" for kilopascals, "bar" for bar)
    convert: desired units of temperature to be converted (specific string - "atm" for atmospheres, "psi" for pounds per square inch, "kPa" for kilopascals, "bar" for bar)
    
    Returns
    -------
    double
        converted value of pressure in given desired units of pressure (atmospheres, pounds per square inch, kilopascals, bar)
    
    Examples
    --------
    initial = 1.0
    pres = "atm"
    convert = "kPa"
    Input: convPres(initial, temp, convert)
    Output: 101.325

    """
    vec = arrPres(initial, pres)
    if (convert == "psi"):
        return vec[3]
    elif (convert == "bar"):
        return vec[2]
    elif (convert == "kPa"):
        return vec[1]
    return vec[0]

print(convVol("L/mol", 1, "m^3/kmol"))

def convVol(initial, vol, convert):
    """
    Converts a volume in given units to another volume in specified units.
    Compatible units are L/mol, m^3/kmol.
    
    
    Parameters
    ----------
    initial: numerical value of volume to be converted (double or int)
    pres: units of initial volume (specific string - "L/mol" for liters per mol, "m^3/kmol" for meters cubed per kilomol)
    convert: desired units of volume to be converted (specific string - "L/mol" for liters per mol, "m^3/kmol" for meters cubed per kilomol)
    
    Returns
    -------
    double
        converted value of volume in given desired units of volume (specific string - "L/mol" for liters per mol, "m^3/kmol" for meters cubed per kilomol)
    
    Examples
    --------
    initial = "L/mol"
    vol = 3.0
    convert = "m^3/kmol"
    Input: convVol(initial, vol, convert)
    Output: 0.003
    """
    if (initial == "L/mol"):
        return vol * 0.001
    return vol * 1000



