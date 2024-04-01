# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 23:03:36 2023

@author: altan
"""
from numpy import zeros

# Parameters regarding time
deltat   = 1e-3;
runtime  = 200;
ni       = round(runtime/deltat)+1;
tplot    = zeros(ni)
time     = 0;
tplot[0] = time;

# Number of states
nos = 2;

# Mechanical System Parameters
A1    = 15.5179;
A2    = 15.5179;
qi    = 5;
kflow = 6;
c1    = 5;
c2    = 5;

# trbdf2 parameter
gammaIvp = 0.5;

stateDotk = zeros(nos);
stateDot1 = zeros(nos);