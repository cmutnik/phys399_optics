# Python script to Fourier Transform data taken with interferomemter
# Corey Mutnik 3/4/16
# http://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.fftconvolve.html#scipy.signal.fftconvolve
from scipy import signal
import numpy as np
from glob import glob
import os
import matplotlib.pyplot as plt

dir_path = u'/Users/cmutnik/work/classes/phys399/c0226/data'
globpath = os.path.join(dir_path, '*.txt')
filelist = glob(globpath)
filelist.sort() # unnecessary


dfile = np.loadtxt(filelist[0])
# sum down columns
#data_y = sum(dfile)
sig = sum(dfile)
# generate x-range
data_x = []
for i in range(len(sig)):
	#pixel2microns = i * 7.4
	data_x.append(i)

#sig = data_y 
#sig = dfile # use for prebinned image
#sig = np.random.randn(1000)
autocorr = signal.fftconvolve(sig, sig[::-1], mode='full')


#autocorr = signal.convolve2d(sig, sig[::-1], boundary='symm', mode='same')


fig, (ax_orig, ax_mag) = plt.subplots(2, 1)
ax_orig.set_xlim([0,640])
ax_orig.plot(sig)
ax_orig.set_title('White noise')
ax_mag.plot(np.arange(-len(sig)+1,len(sig)), autocorr)
ax_mag.set_title('Autocorrelation')
fig.tight_layout()
fig.show()
#plt.savefig(os.path.basename(filelist[0]) + '_fft.png')


