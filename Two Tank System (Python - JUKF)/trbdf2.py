# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 23:28:48 2023

@author: altan
"""
from mathmodel import *

def trbdf2(state,stateDot,time,qi,c1,A1,c2,A2,gammaIvp,deltat,nse,stateDotk,stateDot1):
    statek    = state+gammaIvp*deltat*stateDot;

    stateDotk = mathmodel(statek,stateDotk,time,qi,c1,A1,c2,A2,nse);
    fkgamma   = (stateDotk+stateDot)/2;
    xkgamma   = state+gammaIvp*(deltat/2)*(stateDot+fkgamma);
    time      = time+deltat;
    
    state1    = state+deltat*stateDot;
    stateDot1 = mathmodel(state1,stateDot1,time,qi,c1,A1,c2,A2,nse);
    fk1       = (stateDot1+stateDot)/2;
    state     = (1/(gammaIvp*(2-gammaIvp)))*xkgamma-(((1-gammaIvp)**2)/(gammaIvp*(2-gammaIvp)))*state+((1-gammaIvp)/(2-gammaIvp))*deltat*fk1;
    return state,time