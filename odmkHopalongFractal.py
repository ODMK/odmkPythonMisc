# -*- coding: utf-8 -*-
# *****************************************************************************
# /////////////////////////////////////////////////////////////////////////////
# header begin-----------------------------------------------------------------
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# *****************************************************************************

# __::((odmkHopalongFractal.py))::__

# Python urllib2 example script
# basic web scrape research scripting


# *****************************************************************************
# /////////////////////////////////////////////////////////////////////////////
# header end-------------------------------------------------------------------
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# *****************************************************************************

from __future__ import division
from numpy import sqrt, power

from pylab import scatter, show, cm, axis
from numpy import array ,mean

import matplotlib.pyplot as plt


#def hopalong(x0, y0, n, a=-55, b=-1, c=-42):
def hopalong(x0, y0, n, a=-33, b=45, c=-56):
    def update(x, y):
        x1 = y-x/abs(x)*sqrt(abs(b*x+c))
        y1 = a-x
        return x1, y1
    xx = []
    yy = []
    for _ in range(n):
        x0, y0 = update(x0, y0)
        xx.append(x0)
        yy.append(y0)
    return xx, yy

#x = -1
#y = 10
#n = 40000
x = 2
y = -1
n = 40000
xx, yy = hopalong(x, y, n)
cr = sqrt(power(array(xx) - mean(xx), 2)+power(array(yy) - mean(yy), 2))
fig = plt.figure(num=1, facecolor='silver', edgecolor='k')
scatter(xx, yy, marker='.', c=cr/max(cr), edgecolor='k', cmap=cm.hot, s=56)
axis('equal')
ax = plt.gca()
ax.set_axis_bgcolor("k")
show()
