# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 23:01:18 2023

@author: altan
"""

from numpy import zeros,sqrt,var,random,save
import math
import timeit

from parameters import *
from mathmodel import *
from trbdf2 import *
from plotVars import *

state    = zeros(nos);
stateDot = zeros(nos);

# Needed if there are initial conditions rather than zero
# state[:] = 0,0,0,0

# Plot Variables
statePlot    = zeros((nos,ni));
stateDotPlot = zeros((nos,ni));
# Time plot
tPlot    = zeros(ni);
start = timeit.default_timer()
for i in range(ni):
    statePlot[:,i]    = state;
    stateDotPlot[:,i] = stateDot;
    
    stateDot = mathmodel(state,stateDot,time,kflow,qi,c1,A1,c2,A2,nos);
    tPlot[i] = time;
    state,time = trbdf2(state,stateDot,time,kflow,qi,c1,A1,c2,A2,gammaIvp,deltat,nos,stateDotk,stateDot1);
stop = timeit.default_timer()
execution_time = stop - start
print("Program Executed in "+str(execution_time)) # It returns time in seconds
plotVars(tPlot,statePlot,stateDotPlot);

# Given SNR in dB
snr_db = 30  # Example SNR of 20 dB

# Calculate noise power
signal_power = np.var(statePlot)
snr_linear = 10 ** (snr_db / 10)
noise_power = signal_power / snr_linear

# Calculate noise standard deviation
noise_std = np.sqrt(noise_power)

# Generate Gaussian noise
noise = np.random.normal(0, noise_std, size=statePlot.shape)

# Add noise to the signal
noisy_signal = statePlot + noise
plotVars(tPlot,noisy_signal,stateDotPlot);

with open('measurements.npy', 'wb') as f:
    save(f, noisy_signal)
    