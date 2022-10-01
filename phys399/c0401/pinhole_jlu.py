#######___________from radialprofile_________________________________________________________________________
def azimuthalAverage(image, center=None):
    """
    Calculate the azimuthally averaged radial profile.

    image - The 2D image
    center - The [x,y] pixel coordinates used as the center. The default is 
             None, which then uses the center of the image (including 
             fracitonal pixels).
    
    """
    # Calculate the indices from the image
    y, x = np.indices(image.shape)

    if not center:
        center = np.array([(x.max()-x.min())/2.0, (x.max()-x.min())/2.0])

    r = np.hypot(x - center[0], y - center[1])

    # Get sorted radii
    ind = np.argsort(r.flat)
    r_sorted = r.flat[ind]
    i_sorted = image.flat[ind]

    # Get the integer part of the radii (bin size = 1)
    r_int = r_sorted.astype(int)

    # Find all pixels that fall within each radial bin.
    deltar = r_int[1:] - r_int[:-1]  # Assumes all radii represented
    rind = np.where(deltar)[0]       # location of changed radius
    nr = rind[1:] - rind[:-1]        # number of radius bin
    
    # Cumulative sum to figure out sums for each radius bin
    csim = np.cumsum(i_sorted, dtype=float)
    tbin = csim[rind[1:]] - csim[rind[:-1]]

    radial_prof = tbin / nr

    return radial_prof
#######____________________________________________________________________________________
#http://www.astrobetter.com/blog/2010/03/03/fourier-transforms-of-images-in-python/
#######____________________________________________________________________________________


from scipy import signal, fftpack
import matplotlib.pyplot as plt
import numpy as np
#import pylab as py
#import pyfits
from glob import glob
import os
#import radialProfile



dir_path = u'/Users/cmutnik/work/classes/phys399/c0304/data'
globpath = os.path.join(dir_path, '*.txt')
filelist = glob(globpath)
filelist.sort() # unnecessary

#imgdat = ascii.read(filelist[0])
#imagdat = pyfits.getdata('c0226_0832.fit')
imgdat = np.loadtxt(filelist[8])
basename = os.path.basename(filelist[8])[:-4]
basename
sig_summed = sum(imgdat)
# Take the fourier transform of the image.
F1 = fftpack.fft2(imgdat)

# Now shift the quadrants around so that low spatial frequencies are in
# the center of the 2D fourier transformed image.
F2 = fftpack.fftshift( F1 )
 
# Calculate a 2D power spectrum
psd2D = np.abs( F2 )**2
 
# Calculate the azimuthally averaged 1D power spectrum
#psd1D = radialProfile.azimuthalAverage(psd2D)
psd1D = azimuthalAverage(psd2D)




# Now plot up both
plt.figure(1)
plt.clf()
plt.title('Original Image')
plt.imshow( np.log10( imgdat ), cmap=plt.cm.Greys)
plt.figure(2)
plt.clf()
plt.title('2D power spectrum')
plt.imshow( np.log10( psd2D ))
plt.figure(3)
plt.clf()
plt.semilogy( psd1D )
plt.title('azimuthally averaged 1D power spectrum')
plt.xlabel('Spatial Frequency')
plt.ylabel('Power Spectrum')
plt.figure(4)
plt.clf()
plt.plot(psd1D)
plt.xlabel('Spatial Frequency')
plt.ylabel('not logged Power Spectrum')
plt.figure(5)
plt.clf()
plt.plot(sig_summed)
plt.title('Summed data')
#plt.show()



#'''####------------------------------------------------------------------------------------------
#sig = np.random.randn(1000)
sig = sum(imgdat)
autocorr = signal.fftconvolve(sig, sig[::-1], mode='full')

plt.figure(6)
fig, (ax_orig, ax_mag) = plt.subplots(2, 1)
ax_orig.plot(sig)
ax_orig.set_title('White noise')
ax_mag.plot(np.arange(-len(sig)+1,len(sig)), autocorr)
ax_mag.set_title('Autocorrelation')
fig.tight_layout()
#fig.show()
#'''####------------------------------------------------------------------------------------------
plt.show()
