# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 23:43:37 2023

@author: altan
"""
import matplotlib.pyplot as plt

font = {'family': 'Times New Roman',
        'color':  'black',
        'weight': 'normal',
        'size': 11,
        }

def plotVars(tPlot,statePlot,stateDotPlot):
    fig1 = plt.figure(1)
    line1 = plt.plot(tPlot[:], statePlot[0, :], linestyle='--', linewidth=0.5, color='black')
    plt.grid(linewidth=0.2)
    plt.legend(line1, ['$h_1$'])
    plt.title('$h_1$', fontdict=font)
    plt.xlabel('Time (s)', fontdict=font)
    plt.tick_params(axis='x', labelsize=11)
    plt.tick_params(axis='y', labelsize=11)
    plt.ylabel('Water Height for the First Tank (cm)', fontdict=font)
    fig1.savefig('Svgs/h1.svg')
    
    fig2 = plt.figure(2)
    line2 = plt.plot(tPlot[:], statePlot[1, :], linestyle='--', linewidth=0.5, color='black')
    plt.grid(linewidth=0.2)
    plt.legend(line2, ['$h_2$'])
    plt.title('$h_2$', fontdict=font)
    plt.xlabel('Time (s)', fontdict=font)
    plt.tick_params(axis='x', labelsize=11)
    plt.tick_params(axis='y', labelsize=11)
    plt.ylabel('Water Height for the Second Tank (cm)', fontdict=font)
    fig2.savefig('Svgs/h2.svg')
    