# optcial resonator

reset

set terminal png nocrop enhanced size 900,700 font 'arial,18'
set out 'optical_res.png'

set title 'Optical Resonator'
set ylabel "Divisions"
set xlabel "Micrometer"

set xr[19.8:20.2]
set yr[3:8]

set key off
#set grid

# Gaussian with 2 in numerator for better data
h(x) = A4*exp(-2.0*((x-o4)/s4)**2)+c4
A4=7.5;# height
o4=20;# peak center
c4=3;# continuum
s4=0.2;# width
fit h(x) 'resonator.dat' u 1:2:3 via A4,o4,s4,c4

#plot 'resonator.dat' u 1:2:3 pt 1 lc rgb '#0000FF' ps 1 t 'Data' w yerrorbars
plot 'resonator.dat' u 1:2:4:3 pt 1 lc rgb '#0000FF' ps 1 t 'Data' w xyerrorbars, \
	h(x) lw 2 lt 3 lc rgb '#32CD32' t 'Gaussian'


#degrees of freedom    (FIT_NDF)                        : 8
#rms of residuals      (FIT_STDFIT) = sqrt(WSSR/ndf)    : 0.281215
#variance of residuals (reduced chisquare) = WSSR/ndf   : 0.0790816
#p-value of the Chisq distribution (FIT_P)              : 0.999676
#Final set of parameters            Asymptotic Standard Error
#=======================            ==========================
#A4              = 7.13446          +/- 2.812        (39.41%)
#o4              = 19.9878          +/- 0.001099     (0.005497%)
#s4              = 0.19389          +/- 0.0529       (27.28%)
#c4              = -0.0417449       +/- 2.9          (6947%)





# Gaussian for older data
#g(x) = A3*exp(-2*((x-o3)/s3)**2)+c3
#A3=7.5;# height
#o3=20;# peak center
#c3=3;# continuum
#s3=0.4;# width
#fit g(x) 'resonator.dat' u 5:6:3 via A3,o3,s3,c3
#plot'resonator.dat' u 4:5:3 pt 2 lc rgb '#32CD32' ps 0.5 t 'Old Data' w yerrorbars, \
#	g(x) lw 2 lt 3 lc rgb '#0000FF' t 'Old Gaussian'

#degrees of freedom    (FIT_NDF)                        : 7
#rms of residuals      (FIT_STDFIT) = sqrt(WSSR/ndf)    : 0.204979
#variance of residuals (reduced chisquare) = WSSR/ndf   : 0.0420165
#p-value of the Chisq distribution (FIT_P)              : 0.999906
#Final set of parameters            Asymptotic Standard Error
#=======================            ==========================
#A3              = 5.49948          +/- 0.9098       (16.54%)
#o3              = 19.996           +/- 0.001313     (0.006565%)
#s3              = 0.159419         +/- 0.02         (12.54%)
#c3              = 1.66396          +/- 0.9433       (56.69%)