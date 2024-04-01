# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 23:03:36 2023

@author: altan
"""
from numpy import zeros, concatenate, array, sqrt, eye, load

# Parameters regarding time
deltat   = 1e-3;
runtime  = 200;
ni       = round(runtime/deltat)+1;
time     = 0;

# Number of states
nos = 2;
# Number of states estimated
nse = 3;
# Number of estimated parameters
npar = 1;
# Number of measurements
nMeas = 2;
# Iteration number to measure computational complexity
noIter = 1;

# Mechanical System Parameters
A1    = 15.5179;
A2    = 15.5179;
qi    = 5;
kflow = 6;
c1    = 5;
c2    = 5;

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
r  = 1e-7;
qp = 1e-1;

Px      = 0.5*eye(nse);
Px[2,2] = qp*eye(npar,npar);

Q = q*eye(nse);
R = r*eye(nMeas);

meas=load('measurements.npy');

# UKF related
L      = (2*nse)+1;
txcap  = zeros((1,nse));
Xdot   = zeros((L,nse));
# trbdf2 related
stateDotk = zeros(nse);
stateDot1 = zeros(nse);

