# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 01:18:59 2023

@author: altan
"""
from numpy import multiply, ones, linalg, transpose, diag, dot, multiply, newaxis, array, mean
from sigmapoints import *
from mathmodel import *
from trbdf2 import *

def mjukf(xcap,thetaCap,thetaCapv,time,k,Jm,BR,Jl,g,h,P,ms,gammaUKF,Wm,Wc,nse,Q,R,deltat,gammaIvp,txcap,Xdot,L):   
    # sigma points around x
    X = sigmapoints(xcap,P,gammaUKF);

    for j in range(L):
        Xdot[j,:]   = mathmodel(X[j,:],Xdot[j,:],thetaCapv[j,:],time,k,Jm,BR,Jl,g,h,nse);
        X[j,:],time = trbdf2(X[j,:],Xdot[j,:],thetaCapv[j,:],time,k,Jm,BR,Jl,g,h,gammaIvp,deltat,nse);        
        time        = time-deltat;
        txcap       = txcap+Wm[j]*X[j,:];
        
    Xdev         = X-multiply(ones((L,txcap.shape[1])),txcap);
    transformedP = linalg.multi_dot([transpose(Xdev),diag(Wc),Xdev])+Q;
    
    Y      = X[:,0:4];
    txcap1 = dot(Wm[None,:],Y);
    Xdev1  = Y-multiply(ones((L,txcap1.shape[1])),txcap1);
    
    transformedP1 = linalg.multi_dot([transpose(Xdev1),diag(Wc),Xdev1])+R;
    # Covariances, Gains etc.
    P12 = linalg.multi_dot([transpose(Xdev),diag(Wc),Xdev1]); # transformed cross-covariance  
    K   = dot(P12,linalg.inv(transformedP1));

    xcap = txcap+transpose(dot(K,transpose(ms-txcap1))); # state update
    P    = transformedP-dot(K,transpose(P12));    #covariance update
    time = time + deltat;
    
    thetaCapv = transpose(thetaCap[:,newaxis] - (-0.0025)*((dot((array([[0.3,0.3,0.2,0.2],[0.2,0.2,0.3,0.3]])),(ms[:,newaxis]-transpose(Y))))));
    thetaCap  = mean(thetaCapv,axis=0);         
    return transpose(xcap).reshape([nse,]),P,time,thetaCap,thetaCapv