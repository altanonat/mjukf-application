# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 23:16:46 2023

@author: altan
"""
import numpy as np
from math import sqrt

def mathmodel(state,stateDot,time,kflow,qi,c1,A1,c2,A2,nos):   
    # if time>5:
    #     Ktau = 0.08;
    #     m = 0.35;
    stateDot[0] = (kflow*qi-c1*sqrt(state[0]))/A1;
    stateDot[1] = (c1*sqrt(state[0])-c2*sqrt(state[1]))/A2;
    return stateDot