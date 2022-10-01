import numpy as np
import matplotlib.pyplot as plt
from scipy import signal, special
from glob import glob
import os
#from scipy.signal import blackman

dir_path = u'/Users/cmutnik/work/classes/phys399/c0401/data'
globpath = os.path.join(dir_path, '*.txt')
filelist = glob(globpath)
filelist.sort() # unnecessary


imgdat = np.loadtxt(filelist[0])
n = 10
bessel = special.yn(n,imgdat)

#sph_bessel = special.sph_yn(n,imgdat)


#z_ = np.atleast_2d(imgdat)
#ttt = ax.plot_surface(imgdat,x_,y_,z_)




plt.figure(1)
plt.clf()
plt.subplot(211)
plt.imshow(imgdat)
plt.gca().invert_yaxis()
plt.title('Actual data')

plt.subplot(212)
plt.imshow(bessel)
plt.gca().invert_yaxis()
plt.title('Bessel: n='+str(n))


'''
fzz = open('test.txt', 'w')
fzz.write('# 2\t#filename\n')
for i in range(len(filelist)):
	imgdat = np.loadtxt(filelist[i])
	basename = os.path.basename(filelist[i])[:-4]
	max_pixels = np.where(abs(Pxx_den - max_) == min(abs(Pxx_den - max_)))[0][0]
	fzz.write(str(f2[max_pixels]*7.4) + '\t# ' + str(basename) + '\n')
fzz.close()
'''



def besselinternet():
	#https://github.com/mertdikmen/python-for-vision/blob/master/matplotlib/bessel.py
	from scipy import optimize, special
	from numpy import *
	import matplotlib.pyplot as plt
	plt.ion()

	x = arange(0,10,0.01)

	for k in arange(0.5,5.5):
	     y = special.jv(k,x)
	     plt.plot(x,y)
	     f = lambda x: -special.jv(k,x)
	     #x_max = optimize.fminbound(f,0,10)
	     x_max = optimize.fmin_bfgs(f,1.0)
	     plt.plot([x_max], [special.jv(k,x_max)],'ro')	

	plt.title('Different Bessel functions and their local maxima')
	plt.grid()


def bessel_online():
	def drumhead_height(n, k, distance, angle, t):
		kth_zero = special.jn_zeros(n, k)[-1]
		return np.cos(t) * np.cos(n*angle) * special.jn(n, distance*kth_zero)
	theta = np.r_[0:2*np.pi:50j]
	radius = np.r_[0:1:50j]
	x = np.array([r * np.cos(theta) for r in radius])
	y = np.array([r * np.sin(theta) for r in radius])
	z = np.array([drumhead_height(1, 1, r, theta, 0.5) for r in radius])	

	from mpl_toolkits.mplot3d import Axes3D
	from matplotlib import cm
	fig = plt.figure()
	ax = Axes3D(fig)
	ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.jet)
	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	ax.set_zlabel('Z')
	#plt.show()
bessel_online()

def bessel_airy_from_internet():
	import numpy as np
	import scipy.special
	import matplotlib.pyplot as plt
	# create a figure window
	fig = plt.figure(1, figsize=(9,8))
	# create arrays for a few Bessel functions and plot them
	#x = np.linspace(0, 20, 256)
	x = imgdat
	j0 = scipy.special.jn(0, x)
	j1 = scipy.special.jn(1, x)
	y0 = scipy.special.yn(0, x)
	y1 = scipy.special.yn(1, x)
	ax1 = fig.add_subplot(321)
	ax1.plot(x,j0, x,j1, x,y0, x,y1)
	ax1.axhline(color="grey", ls="--", zorder=-1)
	ax1.set_ylim(-1,1)
	ax1.text(0.5, 0.95,'Bessel', ha='center', va='top',transform = ax1.transAxes)
	# Airy function
	#x = np.linspace(-15, 4, 256)
	ai, aip, bi, bip = scipy.special.airy(x)
	ax4 = fig.add_subplot(324)
	ax4.plot(x,ai, x,bi)
	ax4.axhline(color="grey", ls="--", zorder=-1)
	ax4.axvline(color="grey", ls="--", zorder=-1)
	#ax4.set_xlim(-15,4)
	#ax4.set_ylim(-0.5,0.6)
	#ax4.text(0.5, 0.95,'Airy', ha='center', va='top',transform = ax4.transAxes)
#bessel_airy_from_internet()