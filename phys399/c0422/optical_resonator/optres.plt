# optcial resonator

reset

set terminal png nocrop enhanced size 900,700 font 'arial,18'
set out 'optres.png'

set title 'Optical Resonator'
set ylabel "Divisions"
set xlabel "Micrometer"

set xr[19.8:20.2]
set yr[3:8]

#set key off
set grid

# Gaussian with 2 in numerator for better data
h(x) = A4*exp(-2.0*((x-o4)/s4)**2)+c4
A4=7.5;# height
o4=20;# peak center
c4=3;# continuum
s4=0.2;# width
fit h(x) 'resonator.dat' u 1:2:3 via A4,o4,s4,c4

f(x) = A*sin(d*x) + B*cos(e*x) + C
A=10;
B=10;
C=10;
d=10;
e=10;
fit f(x) 'resonator.dat' u 1:2:3 via A,B,C,d,e

f2(x) = A2*sin(d2*x) + B2*cos(e2*x) + C2
A2=10;
B2=10;
C2=10;
d2=10;
e2=10;
fit f2(x) 'resonator.dat' u 1:2 via A2,B2,C2,d2,e2

g(x) = L*sin(N*x) + M
L=1;
N=1;
M=1;
fit g(x) 'resonator.dat' u 1:2 via L,N,M


plot 'resonator.dat' u 1:2:4:3 pt 1 lc rgb '#0000FF' ps 1 t '' w xyerrorbars, \
	h(x) lw 2 lt 3 lc rgb '#32CD32' t 'Gaussian', \
	g(x) lw 2 lt 5 lc rgb 'blue' t 'Sin', \
	f(x) lw 2 lt 4 lc rgb 'black' t 'SinCos fit w/ err', \
	f2(x) lw 2 lt 4 lc rgb 'red' t 'SinCos fit w/o err'


## Gaussian
#After 8 iterations the fit converged.
#final sum of squares of residuals : 0.632653
#rel. change during last iteration : 0
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

# Sin Cosine with error
#After 2751 iterations the fit converged.
#final sum of squares of residuals : 0.694343
#rel. change during last iteration : -9.99961e-06
#degrees of freedom    (FIT_NDF)                        : 7
#rms of residuals      (FIT_STDFIT) = sqrt(WSSR/ndf)    : 0.314947
#variance of residuals (reduced chisquare) = WSSR/ndf   : 0.0991918
#p-value of the Chisq distribution (FIT_P)              : 0.998379
#Final set of parameters            Asymptotic Standard Error
#=======================            ==========================
#A               = 36.4397          +/- 199          (546.1%)
#B               = 37.6169          +/- 281.1        (747.2%)
#C               = 0.844858         +/- 10.23        (1211%)
#d               = 9.90963          +/- 0.8234       (8.309%)
#e               = 9.99635          +/- 0.7481       (7.484%)

# Sin Cosine no error
#After 2751 iterations the fit converged.
#final sum of squares of residuals : 0.173586
#rel. change during last iteration : -9.99961e-06
#degrees of freedom    (FIT_NDF)                        : 7
#rms of residuals      (FIT_STDFIT) = sqrt(WSSR/ndf)    : 0.157474
#variance of residuals (reduced chisquare) = WSSR/ndf   : 0.024798
#Final set of parameters            Asymptotic Standard Error
#=======================            ==========================
#A2              = 36.4397          +/- 199          (546.1%)
#B2              = 37.6169          +/- 281.1        (747.2%)
#C2              = 0.844858         +/- 10.23        (1211%)
#d2              = 9.90963          +/- 0.8234       (8.309%)
#e2              = 9.99635          +/- 0.7481       (7.484%)

# Sin without error but with offset and amplitude
#After 567 iterations the fit converged.
#final sum of squares of residuals : 0.224657
#rel. change during last iteration : -1.35295e-08
#degrees of freedom    (FIT_NDF)                        : 9
#rms of residuals      (FIT_STDFIT) = sqrt(WSSR/ndf)    : 0.157993
#variance of residuals (reduced chisquare) = WSSR/ndf   : 0.0249619
#Final set of parameters            Asymptotic Standard Error
#=======================            ==========================
#L               = 3651.69          +/- 178.2        (4.879%)
##N               = 0.392943         +/- 2.234e-05    (0.005685%)
#M               = -3644.78         +/- 178.1        (4.887%)

# Sin without error, offset, amplitude
#After 89 iterations the fit converged.
#final sum of squares of residuals : 249.548
#rel. change during last iteration : -9.96066e-06
#degrees of freedom    (FIT_NDF)                        : 11
#rms of residuals      (FIT_STDFIT) = sqrt(WSSR/ndf)    : 4.763
#variance of residuals (reduced chisquare) = WSSR/ndf   : 22.6862
#Final set of parameters            Asymptotic Standard Error
#=======================            ==========================
#N2              = 1.01955          +/- 0.9135       (89.6%)
