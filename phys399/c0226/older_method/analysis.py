# analysis of interferometer data taken 2/26
from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimized		# needed to fit gaussian
import scipy.fftpack					# for fourier transform of 2d array

datafile = 'c0226_0931.txt'
lower = [139,208,272,333]
higher = [208,272,335,403]
filename = '/Users/cmutnik/work/classes/phys399/c0226/data/'+ datafile

# open data
#datafile = fits.getdata('other_file_formats/c0226_0832.fit')
#dhead = fits.getheader('other_file_formats/c0226_0832.fit')
dfile = np.loadtxt(filename)

# sum down columns
data_y = sum(dfile)

# generate x-range
data_x = []
for i in range(len(data_y)):
	data_x.append(i)





'''
# display data
plt.clf()
plt.imshow(dfile)
plt.show()
# display as graph
plt.clf()
plt.plot(data_x, data_y, 'r')
plt.plot(data_y, 'g')
plt.show()
'''

def gaussian(x, a, b, c, d):
    '''
    a = peak height, b = peak center, c = width of peak, d = continuum
    '''
    y = a * np.exp((-(x-b)**2)/(2*c**2)) + d
    return y

#WORKS---------------------------
def Gaussian_plot_of_data():
	lower = 333
	higher = 403
	# slice data
	y_range = data_y[lower:higher]
	x_range = data_x[lower:higher]
	# Gaussian fit
	continuum_= np.min(y_range) 
	width_ = 30#higher-lower
	center_ = np.median(x_range)
	height_ = np.max(y_range)
	a,b,c,d = height_, center_, width_, continuum_ # set function parameters to data values
	param, covar = optimized.curve_fit(gaussian, y_range, x_range, p0=[a,b,c,d])
	print 'height: ', param[0], '\tcenter: ', param[1] , '\twidth: ', param[2] , '\tcontinuum: ', param[3]
	y_plot = gaussian(data_x, param[0], param[1], param[2], param[3]) # plot fit against the x_data
	# plot data
	plt.clf()
	plot_data, = plt.plot(data_x, data_y,'g-', label='binned data')
	gaussians, = plt.plot(data_x, y_plot, label='Gaussian Fits', color='red')	

	plt.title('Interferometer Data Binned')
	plt.xlabel(' \Delta ')
	plt.ylabel('\Gamma')	

	plt.legend(handles=[gaussians, plot_data]) #plot legend
	plt.show()
Gaussian_plot_of_data()



def plot_gauss_all_peaks():
	plt.clf()
	#lower = [139,208,272,333]
	#higher = [208,272,335,403]
	centers_list = []
	for i in range(len(lower)):
		y_range = data_y[lower[i]:higher[i]]
		x_range = data_x[lower[i]:higher[i]]
		continuum_= np.min(y_range) 
		width_ = higher[i]-lower[i]
		center_ = np.median(x_range)
		height_ = np.max(y_range)
		a,b,c,d = height_, center_, width_, continuum_ # set function parameters to data values
		param, covar = optimized.curve_fit(gaussian, y_range, x_range, p0=[a,b,c,d])
		print 'height: ', param[0], '\tcenter: ', param[1] , '\twidth: ', param[2] , '\tcontinuum: ', param[3]
		y_plot = gaussian(data_x, param[0], param[1], param[2], param[3]) # plot fit against the x_data
		gaussians, = plt.plot(data_x, y_plot, label='Gaussian Fits', color='red')
		centers_list.append(param[1])
	print centers_list[0], '\t\t\t', centers_list[1], '\t\t\t', centers_list[2], '\t\t\t', centers_list[3] #' = centers' 
	plot_data, = plt.plot(data_x, data_y,'g-', label='binned data')
	plt.title('Interferometer Data Binned')
	#plt.xlabel(' \Delta ')
	#plt.ylabel('\Gamma')	
	'''
	# text = center to center separation
	string1 = centers_list[1] - centers_list[0]
	string2 = centers_list[2] - centers_list[1]
	string3 = centers_list[3] - centers_list[2]
	plt.text((centers_list[1] + centers_list[0])/2, 560435,string1)
	plt.text((centers_list[2] + centers_list[1])/2, 503681,string2)
	plt.text((centers_list[3] + centers_list[2])/2, 427151,string3)
	'''

	plt.legend(handles=[gaussians, plot_data]) #plot legend
	plt.show()
	#plt.savefig(datafile+'_gaussian_fits.png')
plot_gauss_all_peaks()





def funccos2(x, C1, C2, C3):
	cos2 = C1 * np.cos(C2 * x)**2 + C3
	return cos2

def plot_cos2():
	#lamb = .0006328 # [mm] = 632.8[nm] = 6.328E-7 [m]
	#C1 = (2. * a * np.pi) / (lamb)
	lower = 10#333
	higher = 20#403
	# slice data
	y_range = data_y[lower:higher]
	x_range = data_x[lower:higher]
	# Cosine squared fit
	C1 = 20
	C2 = 20000
	C3 = 500
	paramcos, covarcos = optimized.curve_fit(funccos2, y_range, x_range, p0=[C1,C2,C3])
	print 'amp: ', paramcos[0], ' inside cos2 func: ', paramcos[1], ' shift: ', paramcos[2]
	y_plot_cos = funccos2(data_x, paramcos[0], paramcos[1], paramcos[2])# plot fit against the x_data	
	# plot data
	plt.clf()
	plot_data_cos, = plt.plot(data_x, data_y,'g-', label='binned data')
	cos2label, = plt.plot(data_x, y_plot_cos, label='Cos^2 Fit', color='red')	
	plt.title('Interferometer Data Binned')	
	plt.legend(handles=[cos2label, plot_data_cos]) #plot legend
	plt.show()

#plot_cos2()

def polyfitted():
	ttt = np.poly1d(data_y)
	plt.clf()
	fit, = plt.plot(ttt)
	data, = plt.plot(data_x, data_y,'g-', label='binned data')
	plt.legend()
	plt.show()
polyfitted()

'''
def FT_double_sided(inputdata):
	#Double sided Fourier Transform
	FT2D = scipy.fftpack.fft2(inputdata, axes=(0,0))
	#plt.clf()
	plt.plot(abs(FT2D))
	plt.ylabel('| FT |')
	#plt.ylim(min(FT2D),8000000)
	plt.show()
	#plt.savefig('FT_c0226_0805.png')

FT_double_sided(data_y)
#FT_double_sided(dfile)	




def plotgaussian_onFT(inputdata):
	# get FT data
	fourtrans = scipy.fftpack.fft2(inputdata, axes=(0,0))
	fourtrans = abs(fourtrans)

	# Gaussian fit
	lower = 10#333
	higher = 20#403
	y_range = data_y[lower:higher]
	x_range = data_x[lower:higher]
	continuum_= np.min(y_range) 
	width_ = 5
	center_ = np.median(x_range)
	height_ = np.max(y_range) #26000000
	a,b,c,d = height_, center_, width_, continuum_ # set function parameters to data values
	param, covar = optimized.curve_fit(gaussian, y_range, x_range, p0=[a,b,c,d])
	print 'height: ', param[0], '\tcenter: ', param[1] , '\twidth: ', param[2] , '\tcontinuum: ', param[3]
	y_plot = gaussian(data_x, param[0], param[1], param[2], param[3]) # plot fit against the x_data
	plot_data, = plt.plot(fourtrans,'g-', label='binned data')
	gaussians, = plt.plot(data_x, y_plot, label='Gaussian Fits', color='red')	
	plt.show()

plotgaussian_onFT(data_y)


######_____________________________________________________________________________________________
def hardcoded(inputdata):
	fourtrans = scipy.fftpack.fft2(inputdata, axes=(0,0))
	fourtrans = abs(fourtrans)
	lower = 10
	higher = 20
	y_range = data_y[lower:higher]
	x_range = data_x[lower:higher]
	continuum_= 2200000
	width_ = 5
	center_ = np.median(x_range)
	height_ = 26000000
	a,b,c,d = height_, center_, width_, continuum_ # set function parameters to data values
	param, covar = optimized.curve_fit(gaussian, y_range, x_range, p0=[a,b,c,d])
	print 'height: ', param[0], '\tcenter: ', param[1] , '\twidth: ', param[2] , '\tcontinuum: ', param[3]
	y_plot = gaussian(data_x, param[0], param[1], param[2], param[3]) # plot fit against the x_data
	plot_data, = plt.plot(fourtrans,'g-', label='binned data')
	gaussians, = plt.plot(data_x, y_plot, label='Gaussian Fits', color='red')	
	plt.show()
	#plt.savefig('hardcoded.png')
#hardcoded(data_y)
######_____________________________________________________________________________________________

'''
