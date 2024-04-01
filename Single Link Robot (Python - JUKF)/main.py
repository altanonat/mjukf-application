# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 23:01:18 2023

@author: altan
"""

from numpy import zeros, mean, ones, sqrt
import math
import timeit

from parameters import *
from mathmodel import *
from trbdf2 import *
from plotVars import *
from jukf import *

# If average time elapsed is measured noIter can be different than 1.
timeElapsed = zeros((1,noIter));
for j in range(noIter):
    stateCap    = zeros(nse);
    stateCapDot = zeros(nse);
    # Initial estimate for Ktau
    stateCap[4] = 0.1;
    # Initial estimate for m
    stateCap[5] = 0.15;
    # For measurements
    ms = zeros((2))

    # Plot Variables
    stateCapPlot    = zeros((nse,ni));
    stateCapDotPlot = zeros((nse,ni));

    # Time plot
    tPlot = zeros(ni);
    time  = 0;
    start = timeit.default_timer()
    for i in range(ni):
        # Measurements are taken once five samples
        if ((i-1)%5)==0:
            ms = meas[0:4,i-1];
            tPlot[i] = time;
            stateCap,Px,time = jukf(stateCap,time,k,Jm,BR,Jl,g,h,Px,ms,gammaUKF,Wm,Wc,nse,Q,R,deltat,gammaIvp,txcap,Xdot,L);
            
            stateCapPlot[:,i]    = stateCap;
            stateCapDotPlot[:,i] = stateCapDot;
        else:
            tPlot[i] = time;
            stateCapDot   = mathmodel(stateCap,stateCapDot,time,k,Jm,BR,Jl,g,h,nse);       
            stateCap,time = trbdf2(stateCap,stateCapDot,time,k,Jm,BR,Jl,g,h,gammaIvp,deltat,nse);
            
            stateCapPlot[:,i]    = stateCap;
            stateCapDotPlot[:,i] = stateCapDot;
    stop = timeit.default_timer()
    execution_time = stop - start
    timeElapsed[0,j] = execution_time;
print("Program Executed in "+str(execution_time)) # It returns time in seconds
print("Average Elapsed Time is "+str(mean(timeElapsed))) # It returns time in seconds
thetaReal      = ones((npar,ni));
thetaReal[0,:] = Ktau*thetaReal[0,:];
thetaReal[1,:] = m*thetaReal[1,:];

esterror    = zeros((npar));
esterror[0] = sqrt(mean((thetaReal[0,2000:20001]-stateCapPlot[4,2000:20001])**2));
esterror[1] = sqrt(mean((thetaReal[1,2000:20001]-stateCapPlot[5,2000:20001])**2));
plotVars(tPlot,stateCapPlot,stateCapDotPlot,meas,thetaReal);    