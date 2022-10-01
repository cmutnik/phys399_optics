
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
from scipy import fftpack
import pyfits
import numpy as np
import pylab as py
#import radialProfile
 
#image = pyfits.getdata('c0226_0832.fit')
image = np.loadtxt('c0226_0805.txt')

# Take the fourier transform of the image.
F1 = fftpack.fft2(image)
 
# Now shift the quadrants around so that low spatial frequencies are in
# the center of the 2D fourier transformed image.
F2 = fftpack.fftshift( F1 )
 
# Calculate a 2D power spectrum
psd2D = np.abs( F2 )**2
 
# Calculate the azimuthally averaged 1D power spectrum
#psd1D = radialProfile.azimuthalAverage(psd2D)
psd1D = azimuthalAverage(psd2D)

# Now plot up both
py.figure(1)
py.clf()
py.title('Original Image')
py.imshow( np.log10( image ), cmap=py.cm.Greys)
 
py.figure(2)
py.clf()
py.title('2D power spectrum')
py.imshow( np.log10( psd2D ))

py.figure(3)
py.clf()
py.semilogy( psd1D )
py.title('azimuthally averaged 1D power spectrum')
py.xlabel('Spatial Frequency')
py.ylabel('Power Spectrum')

py.show()

