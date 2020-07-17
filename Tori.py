#Most of this code for outputting the plot of a torus came from https://scipython.com/book/chapter-7-matplotlib/examples/a-torus/
#and was NOT created by me, Jason Bohne, however I did comment the code such that one can change the paramters to
#produce different tori


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# imports essential packages for plotting torus

n = 140
#sets dimensions on plot


theta = np.linspace(0, 2.*np.pi, n)
phi = np.linspace(0, 2.*np.pi, n)
theta, phi = np.meshgrid(theta, phi)
c, a = 4, 1 #c is  the distance from the center of the tube to the center of the torus, , a is the radius of the torus
#sets dimensions for torus to rotate over radius, etc.

x = (c + a*np.cos(theta)) * np.cos(phi)
y = (c + a*np.cos(theta)) * np.sin(phi)
z = a * np.sin(theta)
#converts spherical coordinates to cartesion coordinates

fig = plt.figure()
ax1 = fig.add_subplot(121, projection='3d')
ax1.set_zlim(-3,3)
ax1.plot_surface(x, y, z, rstride=5, cstride=5, color='k', edgecolors='w')
ax1.view_init(36, 26)
ax2 = fig.add_subplot(122, projection='3d')
ax2.set_zlim(-3,3)
ax2.plot_surface(x, y, z, rstride=5, cstride=5, color='k', edgecolors='w')
ax2.view_init(0, 0)
ax2.set_xticks([])
plt.show()
#plots Torus in separate window
