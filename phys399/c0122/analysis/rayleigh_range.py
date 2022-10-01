import numpy as np
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt
import scipy.optimize as optimized


y,x = np.loadtxt('gauss6.dat', unpack=True)


coefs = poly.polyfit(x, y, 2)
ffit = poly.polyval(x, coefs)
print 'coefs:\t', coefs
string1 = 'z_R = ' + str(coefs[0]) + ' [m]'

def plotdatawithfit(fn='rayleigh_range.png'):
	plt.clf()
	plt.xlabel('z [m]')
	plt.ylabel('w [mm]')
	plt.title('Calculate Rayleigh Range of HeNe Laser')
	plt.plot(x/1000.,y,'r.')
	plt.plot(x/1000., ffit, 'g-')
	plt.text(.8,2.5,string1)
	#plt.show()
	plt.savefig(fn)

# call plotting function
plotdatawithfit()


'''
lamb = .0006328 # [mm] = 632.8[nm] = 6.328E-7 [m]

def waist(x,zr,d):
    """equation."""
    return np.sqrt(lamb*zr/np.pi) * np.sqrt(1. + (x**2/zr**2.)) + d

a, d = 10., 0. # initial guess
param1, covar1 = optimized.curve_fit(waist, x, y, p0=[a,d])
y_plot = waist(x, param1[0], param1[1])
plt.clf()
plt.plot((x/1000.), y_plot, '-')
#plt.plot((x/1000.), y, 'o')
'''