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
timeElapsed = zeros((1, noIter))
for j in range(noIter):
    stateCap = zeros(nse)
    stateCapDot = zeros(nse)
    # Initial estimate for
    stateCap[2] = 2
    # For measurements
    ms = zeros((nMeas))

    # Plot Variables
    stateCapPlot = zeros((nse, ni))
    stateCapDotPlot = zeros((nse, ni))

    # Time plot
    tPlot = zeros(ni)
    time = 0
    start = timeit.default_timer()
    for i in range(ni):
        # Measurements are taken once two samples
        if ((i-1) % 2) == 0:
            ms = meas[0:nMeas, i-1]
            tPlot[i] = time
            stateCap, Px, time = jukf(stateCap, time, qi, c1, A1, c2, A2, Px, ms, gammaUKF,
                                      Wm, Wc, nse, Q, R, deltat, gammaIvp, txcap, Xdot, stateDotk, stateDot1, L)

            stateCapPlot[:, i] = stateCap
            stateCapDotPlot[:, i] = stateCapDot
        else:
            tPlot[i] = time
            stateCapDot = mathmodel(stateCap, stateCapDot, time, qi, c1, A1, c2, A2, nse)
            stateCap, time = trbdf2(stateCap, stateCapDot, time, qi, c1,
                                    A1, c2, A2, gammaIvp, deltat, nse, stateDotk, stateDot1)

            stateCapPlot[:, i] = stateCap
            stateCapDotPlot[:, i] = stateCapDot
    stop = timeit.default_timer()
    execution_time = stop - start
    timeElapsed[0, j] = execution_time
print("Program Executed in "+str(execution_time))  # It returns time in seconds
# It returns time in seconds
print("Average Elapsed Time is "+str(mean(timeElapsed)))
thetaReal = ones((npar, ni))
thetaReal[0, :] = kflow*thetaReal[0, :]

esterror = zeros((npar))
esterror[0] = sqrt(mean((thetaReal[0, 20000:ni]-stateCapPlot[2, 20000:ni])**2))
plotVars(tPlot, stateCapPlot, stateCapDotPlot, meas, thetaReal, ni)
