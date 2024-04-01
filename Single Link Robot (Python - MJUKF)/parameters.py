# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 23:03:36 2023

@author: altan
"""
from numpy import concatenate, zeros, array, sqrt, eye, load

# Parameters regarding time
deltat   = 1e-3;
runtime  = 20;
ni       = round(runtime/deltat)+1;
time     = 0;

# Number of states
nos = 4;
# Number of states estimated
nse = 4;
# Number of estimated parameters
npar = 2;
# Number of measurements
nMeas = 4;
# Number of sigma points
L = ((2*nse)+1);
# Iteration number to measure computational complexity
noIter = 1;

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

# UKF Parameters
alphaUKF = 1;    # default, tunable
kappaUKF = 0;    # default, tunable
betaUKF  = 2;    # default, tunable

lambdaUKF = (alphaUKF**2)*(nse+kappaUKF)-nse; # scaling factor
gammaUKF  = nse+lambdaUKF; # scaling factor

# Wieghts for means
Wm       = concatenate((lambdaUKF/gammaUKF, (0.5)/(gammaUKF+zeros(2*nse))),axis=None);
Wc       = array(Wm);
Wc[0]    = Wc[0]+(1-(alphaUKF**2)+betaUKF); # weights for covariance
gammaUKF = sqrt(gammaUKF);

q  = 1e-5;
r  = 1e-3;

Px = 0.5*eye(nse);

Q = q*eye(nse);
R = r*eye(nMeas);

meas=load('measurements.npy');

# UKF related parameters
L      = (2*nos)+1;
txcap  = zeros((1,nse));
Xdot   = zeros((L,nse));