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

def plotVars(tPlot,statePlot,stateDotPlot,meas,thetaReal):
    fig1 = plt.figure(1)
    line1, = plt.plot(tPlot[:], statePlot[0, :], linestyle='solid', linewidth=0.5, color='black')
    plt.legend([line1], ['$\\theta_{m}$'])  # Only show legend for state
    plt.grid(linewidth=0.2)
    plt.title('$\\theta_{m}$ (rad) - (JUKF)', fontdict=font)
    plt.xlabel('Time (s)', fontdict=font)
    plt.tick_params(axis='x', labelsize=11)
    plt.tick_params(axis='y', labelsize=11)
    plt.ylabel('Angular position of the motor - $\\theta_{m}$ (rad)', fontdict=font)
    fig1.savefig('Svgs/thetam-jukf.svg')
    plt.show()
    
    fig2 = plt.figure(2)
    line2, = plt.plot(tPlot[:], statePlot[1, :], linestyle='solid', linewidth=0.5, color='black')
    plt.legend([line2], ['$\\omega_{m}$'])  # Only show legend for state
    plt.grid(linewidth=0.2)
    plt.title('$\\omega_{m}$ (rad/s) - (JUKF)', fontdict=font)
    plt.xlabel('Time (s)', fontdict=font)
    plt.tick_params(axis='x', labelsize=11)
    plt.tick_params(axis='y', labelsize=11)
    plt.ylabel('Angular velocity of the motor - $\\omega_{m}$ (rad/s)', fontdict=font)
    fig2.savefig('Svgs/omegam-jukf.svg')
    plt.show()
    
    fig3 = plt.figure(3)
    line3, = plt.plot(tPlot[:], statePlot[2, :], linestyle='solid', linewidth=0.5, color='black')
    plt.legend([line2], ['$\\theta_{l}$'])  # Only show legend for state
    plt.grid(linewidth=0.2)
    plt.title('$\\theta_{l}$ (rad) - (JUKF)', fontdict=font)
    plt.xlabel('Time (s)', fontdict=font)
    plt.tick_params(axis='x', labelsize=11)
    plt.tick_params(axis='y', labelsize=11)
    plt.ylabel('Angular position of the link - $\\theta_{l}$ (rad)', fontdict=font)
    fig3.savefig('Svgs/thetal-jukf.svg')
    plt.show()
    
    fig4 = plt.figure(4)
    line4, = plt.plot(tPlot[:], statePlot[3, :], linestyle='solid', linewidth=0.5, color='black')
    plt.legend([line2], ['$\\omega_{l}$'])  # Only show legend for state
    plt.grid(linewidth=0.2)
    plt.title('$\\omega_{l}$ (rad/s) - (JUKF)', fontdict=font)
    plt.xlabel('Time (s)', fontdict=font)
    plt.tick_params(axis='x', labelsize=11)
    plt.tick_params(axis='y', labelsize=11)
    plt.ylabel('Angular velocity of the link - $\\omega_{l}$ (rad/s)', fontdict=font)
    fig4.savefig('Svgs/omegal-jukf.svg')
    plt.show()
    
    fig5=plt.figure(5)
    line1, = plt.plot(tPlot[:], statePlot[4, :],linestyle='solid', linewidth=0.5, color='gray')
    line2, = plt.plot(tPlot[:], thetaReal[0, :],linestyle='-.', linewidth=1, color='black')
    plt.legend([line1, line2], ['$\\hat{\\theta}_{1}$', 'Real Value'])
    plt.grid(linewidth=0.2)
    plt.title('$K_{\\tau}$ Estimate - (JUKF)', fontdict=font)
    plt.xlabel('Time (s)', fontdict=font)
    plt.tick_params(axis='x', labelsize=11)
    plt.tick_params(axis='y', labelsize=11)
    # Set y-axis limits to 0 and 10
    plt.ylim(0, 0.25)  # (ymin, ymax)
    plt.ylabel('Parameter Estimate ($k_{\\tau}$)', fontdict=font)  
    fig5.savefig('Svgs/ktau-jukf.svg')
    plt.show()
    
    fig6=plt.figure(6)
    line1, = plt.plot(tPlot[:], statePlot[5, :],linestyle='solid', linewidth=0.5, color='gray')
    line2, = plt.plot(tPlot[:], thetaReal[1, :],linestyle='-.', linewidth=1, color='black')
    plt.legend([line1, line2], ['$\\hat{\\theta}_{2}$', 'Real Value'])
    plt.grid(linewidth=0.2)
    plt.title('$m$ Estimate - (JUKF)', fontdict=font)
    plt.xlabel('Time (s)', fontdict=font)
    plt.tick_params(axis='x', labelsize=11)
    plt.tick_params(axis='y', labelsize=11)
    # Set y-axis limits to 0 and 10
    plt.ylim(0.1, 0.3)  # (ymin, ymax)
    plt.ylabel('Parameter Estimate ($m$)', fontdict=font)  
    fig6.savefig('Svgs/m-jukf.svg')
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
