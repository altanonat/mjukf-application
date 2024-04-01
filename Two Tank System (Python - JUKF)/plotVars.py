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


def plotVars(tPlot, statePlot, stateDotPlot, meas, thetaReal , ni):
    fig1 = plt.figure(1)
    line1, = plt.plot(tPlot[:], statePlot[0, :], linestyle='solid', linewidth=0.5, color='black')
    plt.legend([line1], ['$\\hat{h}_{1}$'])  # Only show legend for state
    plt.grid(linewidth=0.2)
    plt.title('$\\hat{h}_{1}$ (cm) - (JUKF)', fontdict=font)
    plt.xlabel('Time (s)', fontdict=font)
    plt.tick_params(axis='x', labelsize=11)
    plt.tick_params(axis='y', labelsize=11)
    plt.ylabel('Water Level Estimate for the First Tank - $\\hat{h}_{1}$ (cm)', fontdict=font)
    fig1.savefig('Svgs/hath1-jukf.svg')
    plt.show()
    
    fig2 = plt.figure(2)
    line2, = plt.plot(tPlot[:], statePlot[1, :], linestyle='solid', linewidth=0.5, color='black')
    plt.legend([line2], ['$\\hat{h}_{2}$'])  # Only show legend for state
    plt.grid(linewidth=0.2)
    plt.title('$\\hat{h}_{2}$ (cm) - (JUKF)', fontdict=font)
    plt.xlabel('Time (s)', fontdict=font)
    plt.tick_params(axis='x', labelsize=11)
    plt.tick_params(axis='y', labelsize=11)
    plt.ylabel('Water Level Estimate for the Second Tank - $\\hat{h}_{2}$ (cm)', fontdict=font)
    fig2.savefig('Svgs/hath2-jukf.svg')
    plt.show()
    # To plot the estimate and the measurement side-by-side
    # fig1=plt.figure(1)
    # line1, = plt.plot(tPlot[:], statePlot[0, :],linestyle='solid', linewidth=0.5, color='gray')
    # line2, = plt.plot(tPlot[:], meas[0, 0:ni],linestyle=':', linewidth=1, color='black')
    # plt.legend([line1, line2], ['$\\hat{h}_{1}$', 'Measurement'])
    # plt.grid()
    # plt.title('$\\hat{h}_{1}$ (cm) - (JUKF)', fontdict=font)
    # plt.xlabel('Time (s)', fontdict=font)
    # plt.tick_params(axis='x', labelsize=11)
    # plt.tick_params(axis='y', labelsize=11)
    # plt.ylabel('Water Level Estimate for the First Tank - $\\hat{h}_{1}$ (cm)', fontdict=font)  
    # fig1.savefig('Svgs/hath1.svg')
    # plt.show()
    
    # fig2=plt.figure(2)
    # line1, = plt.plot(tPlot[:], statePlot[1, :],linestyle='solid', linewidth=0.5, color='gray')
    # line2, = plt.plot(tPlot[:], meas[1, 0:ni],linestyle=':', linewidth=1, color='black')
    # plt.legend([line1, line2], ['$\\hat{h}_{2}$', 'Measurement'])
    # plt.grid()
    # plt.title('$\\hat{h}_{2}$ (cm) - (JUKF)', fontdict=font)
    # plt.xlabel('Time (s)', fontdict=font)
    # plt.tick_params(axis='x', labelsize=11)
    # plt.tick_params(axis='y', labelsize=11)
    # plt.ylabel('Water Level Estimate for the Second Tank - $\\hat{h}_{2}$ (cm)', fontdict=font)  
    # fig2.savefig('Svgs/hath2.svg')
    # plt.show()
    
    fig3=plt.figure(3)
    line1, = plt.plot(tPlot[:], statePlot[2, :],linestyle='solid', linewidth=0.5, color='gray')
    line2, = plt.plot(tPlot[:], thetaReal[0, :],linestyle='-.', linewidth=1, color='black')
    plt.legend([line1, line2], ['$\\hat{\\theta}$', 'Real Value'])
    plt.grid(linewidth=0.2)
    plt.title('$k_{flow}$ Estimate - (JUKF)', fontdict=font)
    plt.xlabel('Time (s)', fontdict=font)
    plt.tick_params(axis='x', labelsize=11)
    plt.tick_params(axis='y', labelsize=11)
    # Set y-axis limits to 0 and 10
    plt.ylim(0, 10)  # (ymin, ymax)
    plt.ylabel('Parameter Estimate ($k_{flow}$)', fontdict=font)  
    fig3.savefig('Svgs/kflow-jukf.svg')
    plt.show()
