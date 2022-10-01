import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
 
x = np.linspace(-8, 8, 100)
y = np.linspace(-8, 8, 100)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)/R
 
fig = plt.figure()
ax = fig.gca(projection = '3d')
 
surf = ax.plot_surface(X, Y, Z,
                      rstride = 3,
                      cstride = 3,
                      cmap = cm.coolwarm,
                      linewidth = 0.5,
                      antialiased = True)
 
fig.colorbar(surf, 
             shrink=0.8, 
             aspect=16,
             orientation = 'vertical')
 
ax.view_init(elev=60, azim=50)
ax.dist=8 
plt.show()