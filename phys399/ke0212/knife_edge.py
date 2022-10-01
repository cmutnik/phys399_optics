# python scrpt for knife edge analysis

import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as poly
import scipy.optimize as optimized

# import knife edge data
z, t1_x10, t1_x90, t1_deltax, t2_x10, t2_x90, t2_deltax, corrected_t2_deltax = np.loadtxt('knife_edge.dat', unpack=True)
'''
# verify delta x values were calculated correctly
# Trial 1
print 'Trial 1 \nCalc Val\tGiven\n'
for j in range(len(t1_deltax)):
	print abs(t1_x10[j]-t1_x90[j]), '\t', t1_deltax[j]
# Trial 2
print 'Trial 2 \nCalc Val\tGiven\n'
for i in range(len(t2_deltax)):
	print abs(t2_x10[i]-t2_x90[i]), '\t', t2_deltax[i]
'''

print z
z *= 25.4 #convert inches to mm
z += 11. # adds distance from flange
z /= 1000. # converts mm to m
print z
# calculate Rayleigh Range
#waist = 0.7803 * abs(t1_x10 - t1_x90) # trial 1
waist = 0.7803 * abs(t2_x10 - t2_x90)

# USED TO MAKE 'knife_edge_rayleigh_range_baddat.png'
#waist = 0.7803 * t2_deltax
lamb = .6328 # = .0006238 [mm] = 632.8[nm] = 6.328E-7 [m]

def waistfunc(x,zr,m2):
    """equation of waist, zr = rayleigh range, m2 = offset"""
    return np.sqrt(lamb*zr/np.pi) * np.sqrt(1. + ((x-m2)**2/zr**2.))

def plotdatawithproperfit(fn='knife_edge_zr.png'):
	'''plots knife edge data with proper function'''
	zr, m2 = 10., 10. # initial guess
	param1, covar1 = optimized.curve_fit(waistfunc, z, waist, p0=[zr,m2])
	y_plot = waistfunc(z, param1[0], param1[1])

	# start plotting
	plt.clf()
	plt.xlabel('z [m]')
	plt.ylabel('w [mm]')
	plt.title('Uniphase Laser Knife Edge')
	plt.plot(z, y_plot, 'r-')
	plt.plot(z, waist, 'go')
	string = 'z_R [m] : ' + str(param1[0]) + '\noffset [m] : '+ str(param1[1])
	plt.text(.4,1.2,string)
	#plt.show()
	plt.savefig(fn)

# call plottinf function
plotdatawithproperfit()


#improper function plot
'''
coefs = poly.polyfit(z, waist, 2)
ffit = poly.polyval(z, coefs)
print 'coefs:\t', coefs
string1 = 'z_R = ' + str(coefs[0]) + ' [m]'

def plotdatawithfit(fn='knife_edge_rayleigh_range_t2.png'):
	plt.clf()
	plt.xlabel('z [m]')
	plt.ylabel('w [mm]')
	plt.title('Rayleigh Range from Knife Edge')
	#plt.plot(waist/1000.,y,'r.')
	#plt.plot(waist/1000., ffit, 'g-')
	plt.plot(z,waist,'r.')
	plt.plot(z, ffit, 'g-')
	plt.text(.4,1.2,string1)
	#plt.show()
	plt.savefig(fn)
# call plotting function
plotdatawithfit()
'''

# bad data plot
'''
def plotdatawithfitflipped(fn='knife_edge_flipped.png'):
	plt.clf()
	plt.xlabel('z [m]')
	plt.ylabel('w [mm]')
	plt.title('Rayleigh Range from Knife Edge')
	#plt.plot(waist/1000.,y,'r.')
	#plt.plot(waist/1000., ffit, 'g-')
	plt.plot(waist,z,'r.')
	plt.plot(waist, ffit, 'g-')
	plt.text(.4,1.2,string1)
	plt.show()
	#plt.savefig(fn)
plotdatawithfitflipped()
'''














