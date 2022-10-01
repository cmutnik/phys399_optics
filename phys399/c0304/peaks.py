import numpy as np


micrometer = np.genfromtxt('pergram_peaks_with_distances.txt')[:,0]
peaks = np.genfromtxt('pergram_peaks_with_distances.txt')[:,1]
peaks_scaled = np.genfromtxt('pergram_peaks_with_distances.txt')[:,2]

# only using data after alignment
aligned_micrometer = np.genfromtxt('data_after_realignment.txt')[:,0]
aligned_peaks = np.genfromtxt('data_after_realignment.txt')[:,1]
aligned_peaks_scaled = np.genfromtxt('data_after_realignment.txt')[:,2]

plt.clf()
plt.plot(micrometer, peaks, 'bo', label='all data', alpha=0.4)
plt.plot(micrometer, peaks_scaled, 'go', label='all data scaled', alpha=0.4)
plt.plot(aligned_micrometer, aligned_peaks, 'ro', label='all after alignment', alpha=0.4)
plt.plot(aligned_micrometer, aligned_peaks_scaled, 'o',color='black', label='scaled after alignment', alpha=0.4)

plt.legend()
plt.savefig('peaks.png')