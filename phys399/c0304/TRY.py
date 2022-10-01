#http://www.physics.nyu.edu/pine/pymanual/html/chap9/chap9_scipy.html
import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt

datfile = np.genfromtxt('data/c0304_0802.txt')
g = sum(datfile)

t = []
for i in range(len(g)):
	t.append(i)
#t = np.linspace(-10, 10, 101)   # linearly space time array
#g = np.exp(-np.abs(t)/width) * np.sin(2.0*np.pi*freq*t)

dt = t[1]-t[0]       # increment between times in time array

G = fftpack.fft(g)   # FFT of g
f = fftpack.fftfreq(g.size, d=dt) # frequenies f[i] of g[i]
f = fftpack.fftshift(f)     # shift frequencies from min to max
G = fftpack.fftshift(G)     # shift G order to coorespond to f


fig = plt.figure(1, figsize=(8,6), frameon=False)
plt.clf()
ax1 = fig.add_subplot(211)
ax1.plot(t, g)
ax1.set_xlabel('t')
ax1.set_ylabel('g(t)')

ax2 = fig.add_subplot(212)
ax2.plot(f, np.real(G), color='dodgerblue', label='real part')
ax2.plot(f, np.imag(G), color='coral', label='imaginary part')
ax2.legend()
ax2.set_xlabel('f')
ax2.set_ylabel('G(f)')
plt.savefig('TRY.png')

#plt.show()