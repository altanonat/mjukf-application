# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 23:01:18 2023

@author: altan
"""

from numpy import zeros, mean, ones, sqrt
from timeit import default_timer


from parameters import *
from mathmodel import *
from trbdf2 import *
from plotVars import *
from mjukf import *

# If average time elapsed is measured noIter can be different than 1.
timeElapsed = zeros((1,noIter));
for j in range(noIter):
    stateCap    = zeros(nse);
    stateCapDot = zeros(nse);
    thetaCap    = zeros(npar);
    thetaCapv   = zeros((L,npar));

    # Intial parameter estimates
    thetaCap[0] = 0.1;
    thetaCap[1] = 0.15;
    for p in range(npar):
        for r in range(L):
            thetaCapv[r,p]=(thetaCap[p]-0.01*(nse+1))+0.01*r;

    thetaCap = mean(thetaCapv,axis=0);

    # For measurements
    ms = zeros((2))

    # Plot Variables
    stateCapPlot    = zeros((nse,ni));
    stateCapDotPlot = zeros((nse,ni));
    thetaCapPlot    = zeros((npar,ni));
    # Time plot
    tPlot = zeros(ni);
    time  = 0;
    start = default_timer()
    for i in range(ni):
        # Measurements are taken once five samples
        if ((i-1)%5)==0:
            ms = meas[0:4,i-1];
            tPlot[i] = time;
            stateCap,Px,time,thetaCap,thetaCapv = mjukf(stateCap,thetaCap,thetaCapv,time,k,Jm,BR,Jl,g,h,Px,ms,gammaUKF,Wm,Wc,nse,Q,R,deltat,gammaIvp,txcap,Xdot,L);
            
            stateCapPlot[:,i]    = stateCap;
            stateCapDotPlot[:,i] = stateCapDot;
            thetaCapPlot[:,i]    = thetaCap;
        else:
            tPlot[i] = time;
            stateCapDot   = mathmodel(stateCap,stateCapDot,thetaCap,time,k,Jm,BR,Jl,g,h,nse);       
            stateCap,time = trbdf2(stateCap,stateCapDot,thetaCap,time,k,Jm,BR,Jl,g,h,gammaIvp,deltat,nse);
            
            stateCapPlot[:,i]    = stateCap;
            stateCapDotPlot[:,i] = stateCapDot;
            thetaCapPlot[:,i]    = thetaCap;
    stop = default_timer()
    execution_time = stop - start
    timeElapsed[0,j] = execution_time;
print("Program Executed in "+str(execution_time)) # It returns time in seconds
print("Average Elapsed Time is "+str(mean(timeElapsed))) # It returns time in seconds
thetaReal      = ones((npar,ni));
thetaReal[0,0:5000] = Ktau*thetaReal[0,0:5000];
thetaReal[1,0:5000] = m*thetaReal[1,0:5000];

# At t=5 seconds the parameter values are changed
thetaReal[0,5000:30001] = 0.1*thetaReal[0,5000:30001];
thetaReal[1,5000:30001] = 0.3*thetaReal[1,5000:30001];

# esterror    = zeros((npar));
# esterror[0] = sqrt(mean((thetaReal[0,2000:20001]-thetaCapPlot[0,2000:20001])**2));
# esterror[1] = sqrt(mean((thetaReal[1,2000:20001]-thetaCapPlot[1,2000:20001])**2));
plotVars(tPlot,stateCapPlot,stateCapDotPlot,thetaCapPlot,meas,thetaReal);
    