# -*- coding: utf-8 -*-
# *****************************************************************************
# /////////////////////////////////////////////////////////////////////////////
# header begin-----------------------------------------------------------------
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# *****************************************************************************
#
# __::((odmkTrifoldKnot1.py))::__
#
# Python Trifold Knot Scatter Plot
#
#
# *****************************************************************************
# /////////////////////////////////////////////////////////////////////////////
# header end-------------------------------------------------------------------
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# *****************************************************************************

import numpy as np
from numpy import linspace, pi, cos, sin, abs
from pylab import scatter, subplot, cm, show
import matplotlib.pyplot as plt


phi = linspace(0,2*pi,100)
x = sin(phi)+2*sin(2*phi)
y = cos(phi)-2*cos(2*phi)
z = -sin(3*phi)


#s = abs(((y+3)+2)*10)
s = abs(((y+3)+2)*33)

fig = plt.figure(num=1, facecolor='silver', edgecolor='k')
scatter(x, y, c=x, s=s, edgecolor='w', cmap=cm.gist_rainbow)
scatter(x/1.4, y/1.2, c=x, s=s, edgecolor='w', cmap=cm.gist_rainbow_r)
scatter(x/1.8, y/1.5, c=x, s=s, edgecolor='w', cmap=cm.gist_rainbow)
ax = plt.gca()
ax.set_axis_bgcolor("k")


fig = plt.figure(num=2, facecolor='silver', edgecolor='k')
scatter(x, y, c=x, s=s, edgecolor='k', cmap=cm.gist_rainbow)
scatter(x/1.4, y/1.4, c=x, s=s/1.5, edgecolor='k', cmap=cm.gist_rainbow_r)
scatter(x/1.8, y/1.8, c=x, s=s/2.0, edgecolor='k', cmap=cm.gist_rainbow)
scatter(x/2.2, y/2.2, c=x, s=s/2.5, edgecolor='k', cmap=cm.gist_rainbow_r)
scatter(x/2.6, y/2.6, c=x, s=s/3.0, edgecolor='k', cmap=cm.gist_rainbow)
scatter(x/3.0, y/3.0, c=x, s=s/3.5, edgecolor='k', cmap=cm.gist_rainbow_r)
ax = plt.gca()
ax.set_axis_bgcolor("k")


fig = plt.figure(num=3, facecolor='silver', edgecolor='k')
# scatter(x, y, c=x, s=s, edgecolor='w', cmap=cm.gnuplot)
scatter(x/1.4, y/1.4, c=x, s=s/1.5, edgecolor='k', cmap=cm.gnuplot_r)
scatter(x/1.8, y/1.8, c=x, s=s/2.0, edgecolor='k', cmap=cm.gnuplot)
scatter(x/2.2, y/2.2, c=x, s=s/2.5, edgecolor='k', cmap=cm.gnuplot_r)
scatter(x/2.6, y/2.6, c=x, s=s/3.0, edgecolor='k', cmap=cm.gnuplot)
scatter(x/3.0, y/3.0, c=x, s=s/3.5, edgecolor='k', cmap=cm.gnuplot_r)
scatter(x/3.4, y/3.4, c=x, s=s/4.0, edgecolor='k', cmap=cm.gnuplot)
ax = plt.gca()
ax.set_axis_bgcolor("k")


phi = linspace(0,2*pi,300)
x = sin(phi)+2*sin(2*phi)
y = cos(phi)-2*cos(2*phi)
z = -sin(3*phi)

numitr = 23
goldenvec1 = np.ones([numitr])
for j in range(numitr-1):
    goldenvec1[j+1] = 1.2618**(j+1)
    # goldenvec1[j+1] = 1.382**(j+1)    
#goldenvec1 = goldenvec1[::-1]

fig = plt.figure(num=4, facecolor='silver', edgecolor='w')
# scatter(x, y, c=x, s=s, edgecolor='w', cmap=cm.gnuplot)

for j in range(numitr):
    # scatter(x/goldenvec1[j], y/goldenvec1[j], c = x, s = s/goldenvec1[j], edgecolor = 'k', cmap = cm.gnuplot)
#    scatter(x/goldenvec1[j], y/goldenvec1[j], c=x, s=s/(1.618*goldenvec1[j]),
#            edgecolor='k', cmap = (lambda j: cm.gnuplot if (j % 2 == 0) else cm.gnuplot_r)(j))
    scatter(x/goldenvec1[j], y/goldenvec1[j], c=x, s=s/(1*goldenvec1[j]),
            edgecolor='k', cmap = (lambda j: cm.bone if (j % 2 == 0) else cm.bone_r)(j))            

ax = plt.gca()
ax.set_axis_bgcolor("k")

show()
