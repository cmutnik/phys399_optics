# 2d Gaussian fit to data collected with HeNe laser for center values
# use to check saturation linearity

import matplotlib.pyplot as plt
import numpy as np
from numpy import *
from scipy import optimize
from glob import glob
import os
from mpl_toolkits.mplot3d import Axes3D

write_file = 'c0129_linearity_params2.dat'
file = open(write_file, 'w')

dir_path = u'/Users/cmutnik/work/classes/phys399/c0129/data/linearity'


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

def plotcontour():
    plt.clf()
    data = data_file
    plt.matshow(data, cmap=plt.cm.gist_earth_r)
    params = fitgaussian(data)
    fit = gaussian(*params)
    plt.colorbar()
    CS1 = plt.contour(fit(*indices(data.shape)), cmap=plt.cm.copper)#,shrink=0.8)
    #manual_locations = [(500,100),(180,350),(300,160)]
    plt.clabel(CS1,fmt='%2.0f', fontsize=14, inline=1)#,manual=manual_locations,colors='black')
    ax = plt.gca()
    #7.4 [microns per pixel] / 1000 [micons per mm] = [mm]
    (height, x, y, width_x, width_y) = params
    params = params
    plt.text(0.95, 0.05, """height : %.1f\nwidth_x : %.1f\nwidth_y : %.1f""" %(height,width_y,width_x),
            fontsize=16, horizontalalignment='right',
            verticalalignment='bottom', transform=ax.transAxes)
    #plt.colorbar(orientation='horizontal',shrink=0.8)
    #plt.show()
    plt.savefig('contour' + file_name[5:-4] + '.pdf')
    print 'type:', type(params),' params: ', params
    #print params
    # Convert quantities from pixels to mm before printing out
    file.write(str(height) + "\t" + str(y) + "\t" + str(x) + "\t" + str(width_y) + "\t" + str(width_x) +"\t# " + str(file_name) + "\n") #y and x are flipped variables
    print "\n",height,"\n"


in2mm = 25.4



for i in range(len(filelist)):
    data_file = np.loadtxt(filelist[i])
    file_name = os.path.basename(filelist[i])
    plotcontour()

#data_file = np.loadtxt(filelist[-1])
#file_name = os.path.basename(filelist[-1])
#plotcontour()
file.close()
