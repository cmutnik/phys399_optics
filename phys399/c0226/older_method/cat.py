from astropy.io import ascii
import numpy as np


filename = 'inches_29.txt'

#xxx = np.genfromtxt(filename)

cat = ascii.read(filename)
cat.colnames

# subtract peak centers to get deparations (periods)
period1 = cat['peak2'] - cat['peak1']
period2 = cat['peak3'] - cat['peak2']
period3 = cat['peak4'] - cat['peak3']

#print 'periods: ', period1, '\t', period2, '\t', period3, '\n' 