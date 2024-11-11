# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 23:43:37 2023

@author: altan
"""
import matplotlib.pyplot as plt

font = {'family': 'Calibri',
        'color':  'black',
        'weight': 'normal',
        'size': 11,
        }

def plotVars(tPlot,statePlot,stateDotPlot):
    fig1 = plt.figure(1)
    line1, = plt.plot(tPlot[:], statePlot[0, :], linestyle='-.', linewidth=0.5, color='black')
    plt.grid(linewidth=0.2)
    plt.legend([line1], ['$\\theta_{m}$'])
    plt.title('Angular Position of the Motor (rad)', fontdict=font)
    plt.xlabel('Time (s)', fontdict=font)
    plt.tick_params(axis='x', labelsize=11)
    plt.tick_params(axis='y', labelsize=11)
    plt.ylabel('$\\theta_{m}$ (rad)', fontdict=font)
    fig1.savefig('Svgs/thetam.svg')
    
    fig2 = plt.figure(2)
    line2, = plt.plot(tPlot[:], statePlot[1, :], linestyle='-.', linewidth=0.5, color='black')
    plt.grid(linewidth=0.2)
    plt.legend([line2], ['$\\omega_{m}$'])
    plt.title('Angular Velocity of the Motor (rad/s)', fontdict=font)
    plt.xlabel('Time (s)', fontdict=font)
    plt.tick_params(axis='x', labelsize=11)
    plt.tick_params(axis='y', labelsize=11)
    plt.ylabel('$\\omega_{m}$ (rad/s)', fontdict=font)
    fig2.savefig('Svgs/omegam.svg')
    
    fig3 = plt.figure(3)
    line3, = plt.plot(tPlot[:], statePlot[2, :], linestyle='-.', linewidth=0.5, color='black')
    plt.grid(linewidth=0.2)
    plt.legend([line3], ['$\\theta_{l}$'])
    plt.title('Angular Position of the Link (rad)', fontdict=font)
    plt.xlabel('Time (s)', fontdict=font)
    plt.tick_params(axis='x', labelsize=11)
    plt.tick_params(axis='y', labelsize=11)
    plt.ylabel('$\\theta_{l}$ (rad)', fontdict=font)
    fig3.savefig('Svgs/thetal.svg')
    
    fig4 = plt.figure(4)
    line4, = plt.plot(tPlot[:], statePlot[3, :], linestyle='-.', linewidth=0.5, color='black')
    plt.grid(linewidth=0.2)
    plt.legend([line4], ['$\\omega_{l}$'])
    plt.title('Angular Velocity of the Link (rad/s)', fontdict=font)
    plt.xlabel('Time (s)', fontdict=font)
    plt.tick_params(axis='x', labelsize=11)
    plt.tick_params(axis='y', labelsize=11)
    plt.ylabel('$\\omega_{l}$ (rad/s)', fontdict=font)
    fig4.savefig('Svgs/omegal.svg')
        
    
    