# 2d Gaussian fit to data collected with HeNe laser

import matplotlib.pyplot as plt
import numpy as np
from numpy import *
from scipy import optimize
from glob import glob
import os

write_file = 'gauss6.dat'
file = open(write_file, 'w')

dir_path = u'/Users/cmutnik/work/classes/phys399/c0122/data'


globpath = os.path.join(dir_path, '*.txt')
filelist = glob(globpath)
filelist.sort() 


def gaussian(height, center_x, center_y, width_x, width_y):
    """Returns a gaussian function with the given parameters"""
    width_x = float(width_x)
    width_y = float(width_y)
    return lambda x,y: height*exp(-2.*
                (((center_x-x)/width_x)**2+((center_y-y)/width_y)**2))

def moments(data):
    """Returns (height, x, y, width_x, width_y)
    the gaussian parameters of a 2D distribution by calculating its
    moments """
    total = data.sum()
    X, Y = indices(data.shape)
    x = (X*data).sum()/total
    y = (Y*data).sum()/total
    col = data[:, int(y)]
    width_x = sqrt(abs((arange(col.size)-y)**2*col).sum()/col.sum())
    row = data[int(x), :]
    width_y = sqrt(abs((arange(row.size)-x)**2*row).sum()/row.sum())
    height = data.max()
    return height, x, y, width_x, width_y

def fitgaussian(data):
    """Returns (height, x, y, width_x, width_y)
    the gaussian parameters of a 2D distribution found by a fit"""
    params = moments(data)
    errorfunction = lambda p: ravel(gaussian(*p)(*indices(data.shape)) -
                                 data)
    p, success = optimize.leastsq(errorfunction, params)
    return p


#########################
#USE CODE ABOVE
#########################
'''
from pylab import *
def plotcontourpylab():
	data = data_file
	matshow(data, cmap=cm.gist_earth_r)
	params = fitgaussian(data)
	fit = gaussian(*params)
	contour(fit(*indices(data.shape)), cmap=cm.copper)
	ax = gca()
	(height, x, y, width_x, width_y) = params
	text(0.95, 0.05, """
	x : %.1f
	y : %.1f
	width_x : %.1f
	width_y : %.1f""" %(x, y, width_x, width_y),
	        fontsize=16, horizontalalignment='right',
	        verticalalignment='bottom', transform=ax.transAxes)
	show()
	#plt.savefig('pylabs.pdf')
'''
def pix2mm(x):
	return x*7.4/1000.

def plotcontour():
	plt.clf()
	data = data_file
	plt.matshow(data, cmap=plt.cm.gist_earth_r)
	params = fitgaussian(data)
	fit = gaussian(*params)
	plt.colorbar()
	CS1 = plt.contour(fit(*indices(data.shape)), cmap=plt.cm.copper)#,shrink=0.8)
	manual_locations = [(500,100),(180,350),(300,160)]
	plt.clabel(CS1,fmt='%2.0f', fontsize=14, inline=1)#,manual=manual_locations,colors='black')
	ax = plt.gca()
	#7.4 [microns per pixel] / 1000 [micons per mm] = [mm]
	(height, x, y, width_x, width_y) = params
	params = pix2mm(params)

	#x and y's are flipped in fit, so print in reverse order
	plt.text(0.95, 0.05, """x[mm] : %.1f\ny[mm] : %.1f\nwidth_x[mm] : %.1f\nwidth_y[mm] : %.1f""" %(pix2mm(y),pix2mm(x),pix2mm(width_y), pix2mm(width_x)),
	        fontsize=16, horizontalalignment='right',
	        verticalalignment='bottom', transform=ax.transAxes)
	
	#plt.colorbar(orientation='horizontal',shrink=0.8)
	#plt.show()
	plt.savefig('contour' + file_name[5:-4] + '.pdf')
	print 'type:', type(params),' params: ', params
	#print params
	# Convert quantities from pixels to mm before printing out
	height = pix2mm(height)
	x = pix2mm(x)
	y = pix2mm(y)
	width_x = pix2mm(width_x)
	width_y = pix2mm(width_y)
	#file.write(str(height) + "\t" + str(y) + "\t" + str(x) + "\t" + str(width_y) + "\t" + str(width_x) + "\t" + str(dist_z[i]*in2mm)  +  "\t" + str(dist_z[i]) +"\t# " + str(file_name) + "\n") #written to 'gauss5.dat'
	waist_ = np.sqrt(width_x*width_x + width_y*width_y) # needed for 'gauss6.dat': improper way of calculating it
	file.write(str(waist_) + "\t" + str(dist_z[i]*in2mm) + "\n") #writen to 'gauss6.dat'
	#waist_common_den = np.sqrt(width_x*width_x*width_y*width_y)
	#file.write(str(waist_common_den) + "\t" + str(dist_z[i]*in2mm) + "\n") #writen to 'gauss7.dat'
###CHANGE FILE NAME TO NUMBER ONLY??? file_name[6:-4]


#plotcontourpylab()
#plotcontour()
#plt.show()
dist_z = np.loadtxt('gauss.dat')
print dist_z, dist_z.shape
in2mm = 25.4 #convert inches to mm

for i in range(len(filelist)):
	data_file = np.loadtxt(filelist[i])
	file_name = os.path.basename(filelist[i])
	plotcontour()
file.close()
