# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 23:16:46 2023

@author: altan
"""
from math import sin, pi

def mathmodel(state,stateDot,time,k,Jm,BR,Jl,g,h,nos):
    u = 5*sin(2*pi*1*time);
    
    stateDot[0] = state[1];
    stateDot[1] = (k/Jm)*(state[2]-state[0])-(BR/Jm)*state[1]+(state[4]/Jm)*u;
    stateDot[2] = state[3];
    stateDot[3] = -(k/Jl)*(state[2]-state[0])-((state[5]*g*h)/Jl)*sin(state[2]);
    return stateDot