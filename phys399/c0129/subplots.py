import numpy as np
import matplotlib.pyplot as plt
from glob import glob
import os


dir_path = u'/Users/cmutnik/work/classes/phys399/c0129/data/calib'

globpath = os.path.join(dir_path, '*.txt')
filelist = glob(globpath)
filelist.sort() 




plt.clf()
f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')

ax1.imshow(np.loadtxt(filelist[0]))
ax2.imshow(np.loadtxt(filelist[1]))
ax3.imshow(np.loadtxt(filelist[2]))
ax4.imshow(np.loadtxt(filelist[3]))
plt.savefig('subplots.png')