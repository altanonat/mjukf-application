# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 23:16:46 2023

@author: altan
"""
from math import sqrt
from numpy import abs

def mathmodel(state,stateDot,time,qi,c1,A1,c2,A2,nos,thetaCap):   
    # if time>5:
    #     Ktau = 0.08;
    #     m = 0.35;
    stateDot[0] = (thetaCap[0]*qi-c1*sqrt(abs(state[0])))/A1;
    stateDot[1] = (c1*sqrt(abs(state[0]))-c2*sqrt(abs(state[1])))/A2;
    return stateDot