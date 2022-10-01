import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from glob import glob
import os
#from scipy.signal import blackman

dir_path = u'/Users/cmutnik/work/classes/phys399/c0304/data'
globpath = os.path.join(dir_path, '*.txt')
filelist = glob(globpath)
filelist.sort() # unnecessary
fzz = open('periodogram_peaks.txt', 'w')
fzz.write('# max_of_per.gram[microns]\tmax_with_scalefactor[microns]\t#filename\n')
fs = 10e3
scalefactor = 1./10.
fs *= scalefactor
for i in range(len(filelist)):
	imgdat = np.loadtxt(filelist[i])
	x = sum(imgdat)
	f, Pxx_den = signal.periodogram(x)
	#plt.figure(1)
	plt.clf()
	plt.semilogy(f, Pxx_den)
	plt.xlabel('frequency [Hz]')
	plt.ylabel('PSD [V**2/Hz]')
	plt.title('Periodogram')
	basename = os.path.basename(filelist[i])[:-4]
	plt.savefig(basename+'.png')
	# NOT SURE IF THIS (BELOW) IS WHAT IS NEEDED
	'''
	f2, Pxx_spec = signal.periodogram(x, fs, 'flattop', scaling='spectrum')
	plt.figure(2)
	plt.clf()
	plt.semilogy(f2, np.sqrt(Pxx_spec))
	plt.xlabel('frequency [Hz]')
	plt.ylabel('Linear spectrum [V RMS]')

	max_ = np.sqrt(Pxx_spec.max())
	max_pixels = np.where(abs(Pxx_spec - max_) == min(abs(Pxx_spec - max_)))[0][0]
	max_pixels *= scalefactor
	print basename, '\t', int(max_pixels), '\t' , f2[max_pixels]*7.4
	'''
	max_ = np.sqrt(Pxx_den.max())
	max_pixels = np.where(abs(Pxx_den - max_) == min(abs(Pxx_den - max_)))[0][0]
	max_pixels_scaled = max_pixels * scalefactor
	# times 7.4 microns per pixel
	fzz.write(str(f[max_pixels]*7.4) + '\t' + str(f[max_pixels_scaled]*7.4) + '\t# ' + str(basename) + '\n')
	#fzz.write(str(f2[max_pixels]*7.4) + '\t# ' + str(basename) + '\n')

fzz.close()