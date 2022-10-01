import matplotlib.pyplot as plt
import pylab
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.mlab import griddata
from PIL import Image

img = np.loadtxt('c0122_0937.txt', unpack=True)
#img = img[:(len(img)/100)]

x_list = []
y_list = []
z_list = []
def generate_data_lists():
	#index = 0
	for ind_1, sublist in enumerate(img):
		for ind_2, ele in enumerate(sublist):
			#index += 1
			x_list.append(ind_1)
			y_list.append(ind_2)
			z_list.append(ele)
			#x_ = ind_1
			#y_ = ind_2
			#z_ = ele
			#l = ax.scatter(x_, y_, z_, c=z_, cmap=cmhot)
			#print 'plotted: ', index , ' of ', (len(img)*len(sublist)) #307200'
			#fig.colorbar(l)
'''
def project_int_data(fn='prject_int_data2.png'):
	plt.clf()
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	cmhot = plt.cm.get_cmap("hot")
	generate_data_lists()
	#plt.clf()
	x_, y_ = np.meshgrid(x_list, y_list)
	#surf = ax.plot_surface(x_list, y_list, z_list, rstride=1, cstride=1, cmap=cm.coolwarm,linewidth=0, antialiased=False)
	ax.plot_wireframe(x_list, y_list, z_list, rstride=10, cstride=10)
	#plt.show()
	plt.savefig(fn)

#####
#project_int_data()
#####

#plt.clf()
#plt.contourf(img)
#plt.show()
'''
def testtopologymap(fn='topologymap.png'):
	plt.clf()
	generate_data_lists()
	xi = np.linspace(min(x_list), max(x_list))
	yi = np.linspace(min(y_list), max(y_list))
	X, Y = np.meshgrid(xi, yi)
	Z = griddata(x_list, y_list, z_list, xi, yi, interp='linear')	
	fig = plt.figure()
	ax = Axes3D(fig)
	cb =ax.plot_surface(X, Y, Z, rstride=1, cmap=plt.cm.jet, cstride=1,linewidth=1, antialiased=True)#, cmap=cm.jet)
	fig.colorbar(cb, shrink=0.8)
	#fig.colorbar.make_axes(shrink=0.8)
	#plt.show()
	plt.savefig(fn)


testtopologymap()




