##/////////////////////////////////////////////////////////////////////////////////////////////
###############################################################################################
##begin : header
###############################################################################################
##/////////////////////////////////////////////////////////////////////////////////////////////
##
##__<<name=> "odmk_3DPlot" (.py)>>__
##
##
##___::((Cyclic-Zn basic script))::___
##___::((ODMK:JIROBATA:ODERUS MONK:2014))::___

##include components:  <<cyclicZn>>

##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
##This script demonstrates the cyclicZn group basic processing
##Tests multiple plotting methods

##Real time controls: 
##n = number of points on cycle
##m = points skipped when drawing star-polygon

##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

##/////////////////////////////////////////////////////////////////////////////////////////////
###############################################################################################
##end : header
###############################################################################################
##/////////////////////////////////////////////////////////////////////////////////////////////


##/////////////////////////////////////////////////////////////////////////////////////////////
###############################################################################################
##begin : main script
###############################################################################################
##/////////////////////////////////////////////////////////////////////////////////////////////


import numpy as np
import pylab as p
##import matplotlib.axes3d as p3
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.axes3d as p3

from odmkAux import *


#//////////////////////////////////////////////////////////////////////////////
# begin: Ex1 - Sphere Wireframe Plot:------------------------------------------
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# u and v are parametric variables.
# u is an array from 0 to 2*pi, with 100 elements
u = np.linspace(0,2*np.pi,100)
# v is an array from 0 to pi, with 100 elements
v = np.linspace(0,np.pi,100)

# x, y, and z are the coordinates of the points for plotting
# each is arranged in a 100x100 array
x=10*np.outer(np.cos(u),np.sin(v))
y=10*np.outer(np.sin(u),np.sin(v))
z=10*np.outer(np.ones(np.size(u)),np.cos(v))


fig1 = plt.figure(num=1, facecolor=mplot_olive, edgecolor='k')
ax1 = p3.Axes3D(fig1)
ax1.plot_wireframe(x,y,z, color=mplot_olive)
#ax1.plot_wireframe(x,y,z, cmap=plt.cm.bone)
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')

#//////////////////////////////////////////////////////////////////////////////
# end: Ex1 - Sphere Wireframe Plot:--------------------------------------------
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


#//////////////////////////////////////////////////////////////////////////////
# begin: Ex2 - Sphere Scatter Plot:--------------------------------------------
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

fig2 = plt.figure(num=2, facecolor=mplot_olive, edgecolor='k')
ax2 = p3.Axes3D(fig2)
# scatter3D requires a 1D array for x, y, and z
# ravel() converts the 100x100 array into a 1x10000 array
ax2.scatter3D(np.ravel(x),np.ravel(y),np.ravel(z))
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')

#//////////////////////////////////////////////////////////////////////////////
# end: Ex2 - Sphere Scatter Plot:----------------------------------------------
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


#//////////////////////////////////////////////////////////////////////////////
# begin: Ex3 - Sphere Surface Plot:--------------------------------------------
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

fig3 = plt.figure(num=3, facecolor=mplot_silver, edgecolor='k')
ax3 = p3.Axes3D(fig3)
# x, y, and z are 100x100 arrays
ax3.plot_surface(x,y,z,color=mplot_purple)
ax3.set_xlabel('X')
ax3.set_ylabel('Y')
ax3.set_zlabel('Z')

#//////////////////////////////////////////////////////////////////////////////
# end: Ex3 - Sphere Surface Plot:----------------------------------------------
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


#//////////////////////////////////////////////////////////////////////////////
# begin: Ex4 - Multi Sphere Wireframe Plot:------------------------------------------
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# u and v are parametric variables.
# u is an array from 0 to 2*pi, with 50 elements
u = np.linspace(0,2*np.pi,50)
# v is an array from 0 to pi, with 50 elements
v = np.linspace(0,np.pi,50)

# x, y, and z are the coordinates of the points for plotting
# each is arranged in a 100x100 array
x=10*np.outer(np.cos(u),np.sin(v))
y=10*np.outer(np.sin(u),np.sin(v))
z=10*np.outer(np.ones(np.size(u)),np.cos(v))

xx=7*np.outer(np.cos(u),np.sin(v))
yy=7*np.outer(np.sin(u),np.sin(v))
zz=7*np.outer(np.ones(np.size(u)),np.cos(v))

fig4 = plt.figure(num=4, facecolor=mplot_olive, edgecolor='k')
ax1 = p3.Axes3D(fig4)
ax1.plot_wireframe(x,y,z, color=mplot_olive)
ax1.plot_wireframe(xx+30,yy,zz, color=mplot_maroon)
ax1.plot_wireframe(xx-30,yy,zz, color=mplot_maroon)
ax1.plot_wireframe(xx,yy+30,zz, color=mplot_maroon)
ax1.plot_wireframe(xx,yy-30,zz, color=mplot_maroon)
ax1.plot_wireframe(xx,yy,zz+30, color=mplot_purple)
ax1.plot_wireframe(xx,yy,zz-30, color=mplot_purple)
#ax1.plot_wireframe(x,y,z, cmap=plt.cm.bone)
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')

#//////////////////////////////////////////////////////////////////////////////
# end: Ex4 - Multi Sphere Wireframe Plot:--------------------------------------
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


#//////////////////////////////////////////////////////////////////////////////
# begin: Ex5 - wire Sphere with box & arrow Plot:------------------------------
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

from itertools import product, combinations

fig5 = plt.figure(num=5, facecolor=mplot_olive, edgecolor='k')

ax5 = fig5.gca(projection='3d')
ax5.set_aspect("equal")

#draw cube
r = [-1, 1]
for s, e in combinations(np.array(list(product(r,r,r))), 2):
    if np.sum(np.abs(s-e)) == r[1]-r[0]:
        ax5.plot3D(*zip(s,e), color="b")

#draw sphere
u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x=np.cos(u)*np.sin(v)
y=np.sin(u)*np.sin(v)
z=np.cos(v)
ax5.plot_wireframe(x, y, z, color="r")

#draw a point
ax5.scatter([0],[0],[0],color="g",s=100)

#draw a vector
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)

a = Arrow3D([0,1],[0,1],[0,1], mutation_scale=20, lw=1, arrowstyle="-|>", color="k")
ax5.add_artist(a)


#//////////////////////////////////////////////////////////////////////////////
# end: Ex5 - wire Sphere with box & arrow Plot:--------------------------------
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


#//////////////////////////////////////////////////////////////////////////////
# begin: Ex20 - Parametric 3D Line Plot 1---------------------------------------
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

plt.rcParams['legend.fontsize'] = 10

fig20 = plt.figure(num=20, facecolor=mplot_silver, edgecolor='k')
ax = fig20.gca(projection='3d')
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)
ax.plot(x, y, z, label='parametric curve')
ax.legend()

#//////////////////////////////////////////////////////////////////////////////
# end: Ex20 - parametric 3D Line Plot 1-----------------------------------------
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


#//////////////////////////////////////////////////////////////////////////////
# begin: Ex21 - Parametric 3D Scatter Plot 1------------------------------------
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

fig21 = plt.figure(num=21, facecolor=mplot_silver, edgecolor='k')
ax = plt.axes(projection='3d')

z = np.linspace(0, 1, 100)
x = z * np.sin(20 * z)
y = z * np.cos(20 * z)

c = x + y

ax.scatter(x, y, z, c=c)

#//////////////////////////////////////////////////////////////////////////////
# end: Ex21 - parametric 3D Scatter Plot 1--------------------------------------
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


#//////////////////////////////////////////////////////////////////////////////
# begin: Ex30 - Cascaded Bar Plot-----------------------------------------------
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

fig30 = plt.figure(num=30, facecolor=mplot_silver, edgecolor='k')
ax = fig30.add_subplot(111, projection='3d')


nBars = 50
rows = [0, 20, 40, 60, 80, 100, 120, 140, 160]

#define the color map
c = plt.cm.Spectral(np.linspace(0.1, 1.0, len(rows)))

#iterator c -> y,r,b,g ; z => 0,20,40,60
#for c, z in zip(['y', 'r', 'b', 'g'], [0, 20, 40, 60]):
for i in range(len(rows)):    
    xs = np.arange(nBars)
    ys = np.random.rand(nBars)

    # You can provide either a single color or an array. To demonstrate this,
    # the first bar of each set will be colored cyan.
    cs = np.repeat(c[i],len(xs)).reshape(4,len(xs)).T
    #cs[0] = 'c'
    ax.bar(xs, ys, zs=rows[i], zdir='y', color=cs, alpha=0.9)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

#//////////////////////////////////////////////////////////////////////////////
# end: Ex30 - Cascaded Bar Plot-------------------------------------------------
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


#//////////////////////////////////////////////////////////////////////////////
# begin: Ex40 - 3D->2D projection plot-----------------------------------------
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

alpha = 0.7
phi_ext = 2*np.pi* 0.5

def flux_qubit_potential(phi_m, phi_p):
    return 2 + alpha - 2 * np.cos(phi_p)*np.cos(phi_m) - alpha * np.cos(phi_ext - 2*phi_p)

phi_m = np.linspace(0, 2*np.pi, 100)
phi_p = np.linspace(0, 2*np.pi, 100)
X,Y = p.meshgrid(phi_p, phi_m)
Z = flux_qubit_potential(X, Y).T

fig40a = plt.figure(num=40,figsize=(14,6))

# `ax` is a 3D-aware axis instance because of the projection='3d' keyword argument to add_subplot
ax40a = fig40a.add_subplot(1, 2, 1, projection='3d')

surf40 = ax40a.plot_surface(X, Y, Z, rstride=4, cstride=4, linewidth=0)

# surface_plot with color grading and color bar
ax40a = fig40a.add_subplot(1, 2, 2, projection='3d')
surf40 = ax40a.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.gist_stern, linewidth=0, antialiased=False)
cb = fig40a.colorbar(surf40, shrink=0.5)


fig40b = plt.figure(num=41,figsize=(8,6))

ax40b = fig40b.add_subplot(1,1,1, projection='3d')

ax40b.plot_surface(X, Y, Z, rstride=4, cstride=4, alpha=0.25)
cset = ax40b.contour(X, Y, Z, zdir='z', offset=-np.pi, cmap=plt.cm.gist_ncar)
cset = ax40b.contour(X, Y, Z, zdir='x', offset=-np.pi, cmap=plt.cm.gist_ncar)
cset = ax40b.contour(X, Y, Z, zdir='y', offset=3*np.pi, cmap=plt.cm.gist_ncar)

ax40b.set_xlim3d(-np.pi, 2*np.pi);
ax40b.set_ylim3d(0, 3*np.pi);
ax40b.set_zlim3d(-np.pi, 2*np.pi);


plt.show()