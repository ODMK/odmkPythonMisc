# -*- coding: utf-8 -*-
# *****************************************************************************
# /////////////////////////////////////////////////////////////////////////////
# header begin-----------------------------------------------------------------
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# *****************************************************************************

# __::((odmkPlotUtil.py))::__

# Python ODMK plotting functions

# *****************************************************************************
# /////////////////////////////////////////////////////////////////////////////
# header end-------------------------------------------------------------------
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# *****************************************************************************

import numpy as np
import matplotlib.pyplot as plt


# // *---------------------------------------------------------------------* //
# // *--Plot Functions--*
# // *---------------------------------------------------------------------* //

def odmkPlot1D(fnum, sig, xLin, pltTitle, pltXlabel, pltYlabel, lncolor='red', lnstyle='-', lnwidth=1.00, pltGrid=True, pltBgColor='black'):
    ''' ODMK 1D Matplotlib plot
        required inputs:
        fnum => unique plot number
        sig => signal to plot
        xLin => linear space to define x-axis (0 to max x-axis length-1)
        pltTitle => text string for plot title
        pltXlabel => text string for x-axis
        pltYlabel => text string for y-axis
        optional inputs:
        lncolor => line color (default = red ; html color names, html color codes??)
        lnstyle => line style (default = plain line ; * ; o ; etc..)
        lnwidth => line width
        pltGrid => use grid : default = True ; <True;False>
        pltBgColor => backgroud color (default = black) '''

    plt.figure(num=fnum, facecolor='silver', edgecolor='k')
    # check if xLin is < than or = to sig
    if len(xLin) > len(sig):
        print('ERROR (odmkPlot1D): length of xLin x-axis longer than signal length - fnum = '+str(fnum))
        return 1
    elif len(xLin) == len(sig):
        odmkMatPlt = plt.plot(xLin, sig)
    else:
        odmkMatPlt = plt.plot(xLin, sig[0:len(xLin)])

    plt.setp(odmkMatPlt, color=lncolor, ls=lnstyle, linewidth=lnwidth)
    plt.xlabel(pltXlabel)
    plt.ylabel(pltYlabel)
    plt.title(pltTitle)
    plt.grid(color='c', linestyle=':', linewidth=.5)
    plt.grid(pltGrid)
    # plt.xticks(np.linspace(0, Fs/2, 10))
    ax = plt.gca()
    ax.set_axis_bgcolor(pltBgColor)

    return 0
    
def odmkMultiPlot1D(fnum, sigArray, xLin, pltTitle, pltXlabel, pltYlabel, colorMp='gnuplot', lnstyle='-', lnwidth=1.00, pltGrid=True, pltBgColor='black'):
    ''' ODMK 1D Matplotlib multi-plot
        required inputs:
        fnum => unique plot number
        sigArray => signal to plot : 2D Numpy array
        xLin => linear space to define x-axis (0 to max x-axis length-1)
        pltTitle => text string for plot title
        pltXlabel => text string for x-axis
        pltYlabel => text string for y-axis
        optional inputs:
        lncolor => line color (default = red ; html color names, html color codes??)
        lnstyle => line style (default = plain line ; * ; o ; etc..)
        lnwidth => line width
        pltGrid => use grid : default = True ; <True;False>
        pltBgColor => backgroud color (default = black) '''

    # define the color map
    try:
        cmap = plt.cm.get_cmap(colorMp)
    except ValueError as e:
        print('ERROR (odmkMultiPlot1D) ValueError: ', e)
    colors = cmap(np.linspace(0.0, 1.0, len(sigArray[:, 0])))

    plt.figure(num=fnum, facecolor='silver', edgecolor='k')
    # check if xLin is < than or = to sig
    if len(xLin) > len(sigArray[0, :]):
        print('ERROR (odmkMultiPlot1D): length of xLin x-axis longer than signal length - fnum = '+str(fnum))
        return 1
    else:
        if len(xLin) == len(sigArray[0, :]):
            # odmkMatPlt = []
            for i in range(len(sigArray[:, 0])):
                plt.plot(xLin, sigArray[i, :], color=colors[i], ls=lnstyle, linewidth=lnwidth)
        else:
            # odmkMatPlt = []
            for i in range(len(sigArray[:, 0])):
                plt.plot(xLin, sigArray[i, 0:len(xLin)], color=colors[i], ls=lnstyle, linewidth=lnwidth)

        plt.xlabel(pltXlabel)
        plt.ylabel(pltYlabel)
        plt.title(pltTitle)
        plt.grid(color='c', linestyle=':', linewidth=.5)
        plt.grid(pltGrid)
        # plt.xticks(np.linspace(0, Fs/2, 10))
        ax = plt.gca()
        ax.set_axis_bgcolor(pltBgColor)

    return 0


    #//////////////////////////////////////////////////////////////////////////
    # begin: Ex30 - Cascaded Bar Plot------------------------------------------
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def odmkBarPlot3D(fnum, sigArray, pltTitle, pltXlabel, pltYlabel, pltZlabel, colorMp='gnuplot', pltGrid=True, pltBgColor='black'):
    ''' ODMK 3D Matplotlib bar plot
        required inputs:
        fnum => unique plot number
        sig => signal to plot : 2D Numpy array
        pltTitle => text string for plot title
        pltXlabel => text string for x-axis
        pltYlabel => text string for y-axis
        pltZlabel => text string for z-axis
        optional inputs:
        pltGrid => use grid : default = True ; <True;False>
        pltBgColor => backgroud color (default = black) '''

    # define the color map
    try:
        cmap = plt.cm.get_cmap(colorMp)
    except ValueError as e:
        print('ERROR (odmkBarPlot3D) ValueError: ', e)
    colors = cmap(np.linspace(0.0, 1.0, len(sigArray[0, :])))     # ?
    # colors = plt.cm.Spectral(np.linspace(0.1, 1.0, len(rows)))
    
    figbp = plt.figure(num=fnum, facecolor='silver', edgecolor='k')    

    ax = figbp.add_subplot(111, projection='3d')
    
    nBars = len(sigArray[:, 0])     # ex: NFFT / 2
    # create an evenly spaced array for num frames
    rows = np.array([])
    for j in range(len(sigArray[0, :])):
        rows = np.append(rows, j*20)     # num of frames
    
    
    #iterator c -> y,r,b,g ; z => 0,20,40,60
    #for c, z in zip(['y', 'r', 'b', 'g'], [0, 20, 40, 60]):
    for i in range(len(rows)):    
        xs = np.arange(nBars)
        ys = np.arange(len(sigArray[i, :]))
        zs = sigArray[:, i]
    
        # You can provide either a single color or an array. To demonstrate this,
        # the first bar of each set will be colored cyan.
        cs = np.repeat(colors[i],len(xs)).reshape(4,len(xs)).T
        #cs[0] = 'c'
        ax.bar(xs, ys, zs, zdir='y', color=cs, alpha=0.9)
    
    ax.set_xlabel('pltXlabel')
    ax.set_ylabel('pltYlabel')
    ax.set_zlabel('pltZlabel')
    
    #pdb.set_trace()
    
    #//////////////////////////////////////////////////////////////////////////
    # end: Ex30 - Cascaded Bar Plot--------------------------------------------
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\