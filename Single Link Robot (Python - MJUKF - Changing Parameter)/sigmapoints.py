# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 01:22:23 2023

@author: altan
"""

from numpy import linalg, multiply, ones, vstack
def sigmapoints(x,P,gamma):
 # Sigma points around reference point
 # Inputs: 
 # x:     reference point
 # P:     covariance
 # gamma: scaling parameter
 # Output:
 # X: Sigma points
 A = gamma*linalg.cholesky(P);
 Y = multiply(ones((x.size,x.size)),x);
 X = vstack((x, Y+A, Y-A));
 return X