from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

n_angles = 36
n_radii = 8

# An array of radii
# Does not include radius r=0, this is to eliminate duplicate points
radii = np.linspace(0.125, 1.0, n_radii)

# An array of angles
angles = np.linspace(0, 2*np.pi, n_angles, endpoint=False)

# Repeat all angles for each radius
angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)

# Convert polar (radii, angles) coords to cartesian (x, y) coords
# (0, 0) is added here. There are no duplicate points in the (x, y) plane
x = np.append(0, (radii*np.cos(angles)).flatten())
y = np.append(0, (radii*np.sin(angles)).flatten())

# Pringle surface
z = np.sin(-x*y)

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot_trisurf(x, y, z, cmap=cm.jet, linewidth=0.2)

plt.show()


#####
# WIRE FRAME
#####
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
 
x = np.linspace(-8, 8, 80)
y = np.linspace(-8, 8, 80)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)/R
 
fig = plt.figure()
ax = fig.gca(projection = '3d')
 
wiref = ax.plot_wireframe(X, Y, Z)
 
ax.view_init(elev=60, azim=50)
ax.dist=8 
plt.show()

#####
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
 
x = np.linspace(-8, 8, 80)
y = np.linspace(-8, 8, 80)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)/R
 
fig = plt.figure()
ax = fig.gca(projection = '3d')
 
wiref = ax.plot_wireframe(X, Y, Z,
                      rstride = 3,
                      cstride = 3,
                      color = 'darkviolet',
                      linewidth = 0.5,
                      antialiased = True)
 
ax.view_init(elev=60, azim=50)
ax.dist=8 
plt.show()