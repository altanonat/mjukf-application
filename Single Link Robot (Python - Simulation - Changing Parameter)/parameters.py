# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 23:03:36 2023

@author: altan
"""
import numpy as np

# Parameters regarding time
deltat   = 1e-3;
runtime  = 30;
ni       = round(runtime/deltat)+1;
tplot    = np.zeros(ni)
time     = 0;
tplot[0] = time;

# Number of states
nos = 4;

# Mechanical System Parameters
Jm   = 3.7e-3;
Jl   = 9.3e-3;
m    = 2.1e-1;
h    = 3e-1;
k    = 4e-1;
BR   = 4.6e-2;
Ktau = 15e-2; # First condition is different from the article
g    = 9.81;

# trbdf2 parameter
gammaIvp = 0.5;