import matplotlib.pyplot as plt
import numpy as np
#[X, Y] = np.meshgrid(2 * np.pi * np.arange(200) / 12,2 * np.pi * np.arange(200) / 34)
#S = np.sin(X) + np.cos(Y) + np.random.uniform(0, 1, X.shape)
S = np.loadtxt('c0226_0805.txt')
FS = np.fft.fftn(S)

#plt.figure(3)
#plt.clf()
#plt.imshow(np.log(np.abs(np.fft.fftshift(FS))**2))


binned = sum(np.log(np.abs(np.fft.fftshift(FS))**2))

#step1 = np.fft.fftshift(FS)
shiftmodsq = np.abs(np.fft.fftshift(FS))**2
#step3 = np.log(shiftmodsq)
logandbin = sum(np.log(shiftmodsq))

plt.figure(1)
plt.clf()
plt.plot(shiftmodsq)
plt.title('shift mod squared')
#plt.savefig('FFT_mine1_0805.png')


plt.figure(2)
plt.clf()
plt.plot(logandbin)
plt.title('log of binned')
#plt.savefig('FFT_mine2_0805.png')
plt.show()