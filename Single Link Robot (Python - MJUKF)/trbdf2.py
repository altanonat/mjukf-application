# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 23:28:48 2023

@author: altan
"""
from mathmodel import *

def trbdf2(state,stateDot,thetaCap,time,k,Jm,BR,Jl,g,h,gammaIvp,deltat,nos):
    statek    = state+gammaIvp*deltat*stateDot;
    fkgamma   = mathmodel(statek,stateDot,thetaCap,time,k,Jm,BR,Jl,g,h,nos);
    xkgamma   = state+gammaIvp*(deltat/2)*(stateDot+fkgamma);
    time      = time+deltat;
    
    state1    = state+deltat*stateDot;
    stateDot1 = mathmodel(state1,stateDot,thetaCap,time,k,Jm,BR,Jl,g,h,nos);
    state     = (1/(gammaIvp*(2-gammaIvp)))*xkgamma-(((1-gammaIvp)**2)/(gammaIvp*(2-gammaIvp)))*state+((1-gammaIvp)/(2-gammaIvp))*deltat*stateDot1;
    return state,time