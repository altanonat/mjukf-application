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
    thetaCap[0] = 2;
    for p in range(npar):
        for r in range(L):
            thetaCapv[r,p]=(thetaCap[p]-0.1*(nse+1))+0.1*r;

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
        # Measurements are taken once two samples
        if ((i-1)%2)==0:
            ms = meas[0:4,i-1];
            tPlot[i] = time;
            stateCap,Px,time,thetaCap,thetaCapv = mjukf(stateCap,time,qi,c1,A1,
                                                        c2,A2,Px,ms,gammaUKF,Wm,Wc,nse,Q,R,deltat,gammaIvp,thetaCap,thetaCapv,txcap,Xdot,stateDotk,stateDot1,L);
            
            stateCapPlot[:,i]    = stateCap;
            stateCapDotPlot[:,i] = stateCapDot;
            thetaCapPlot[:,i]    = thetaCap;
        else:
            tPlot[i] = time;
            stateCapDot   = mathmodel(stateCap,stateCapDot,time,qi,c1,A1,c2,A2,nse,thetaCap);       
            stateCap,time = trbdf2(stateCap, stateCapDot,time,qi,c1,
                                    A1,c2,A2,gammaIvp,deltat,nse,thetaCap,stateDotk,stateDot1);
            
            stateCapPlot[:,i]    = stateCap;
            stateCapDotPlot[:,i] = stateCapDot;
            thetaCapPlot[:,i]    = thetaCap;
    stop = default_timer()
    execution_time = stop - start
    timeElapsed[0,j] = execution_time;
print("Program Executed in "+str(execution_time)) # It returns time in seconds
print("Average Elapsed Time is "+str(mean(timeElapsed))) # It returns time in seconds
thetaReal = ones((npar, ni))
thetaReal[0, :] = kflow*thetaReal[0, :]

esterror = zeros((npar))
esterror[0] = sqrt(mean((thetaReal[0, 20000:ni]-thetaCapPlot[0, 20000:ni])**2))
plotVars(tPlot,stateCapPlot,stateCapDotPlot,thetaCapPlot,meas,thetaReal,ni);
    