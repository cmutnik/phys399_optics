ers = 1
mm2microns = 1000.

set term png
set out 'calib_fits.png'
set fit errorvariables
set key off

set xlabel 'Pixels'
set ylabel 'Microns'
set title 'Calibration: f(x) = ax + b'

f1(x) = a*x + b
a = 1;
b = 1;
fit f1(x) 'c0129_gauss_fit_params.dat' u 2:($4*mm2microns) via a,b

set label 1 sprintf("X^2 = %3.5g",FIT_STDFIT**2) at 350,4500 font "arialbd,15" tc lt 2
set label 2 sprintf("a = %3.5f+/-%3.5f",a,a_err) at 350,4000 font "arialbd,15" tc lt 2
set label 3 sprintf("b = %3.2f+/-%3.2f",b,b_err) at 350,3500 font "arialbd,15" tc lt 2
set label 7 sprintf("X Data") at 350,5000 font "arialbd,15" tc lt 2

f2(x) = c*x + d
c = 1;
d = 1;
fit f2(x) 'c0129_gauss_fit_params.dat' u 3:($5*mm2microns) via c,d

set label 4 sprintf("X^2 = %3.5g",FIT_STDFIT**2) at 30,10000 font "arialbd,15" tc lt 1
set label 5 sprintf("a = %3.5f+/-%3.5f",c,c_err) at 30,9500 font "arialbd,15" tc lt 1
set label 6 sprintf("b = %3.2f+/-%3.2f",d,d_err) at 30,9000 font "arialbd,15" tc lt 1
set label 8 sprintf("Y Data") at 30,10500 font "arialbd,15" tc lt 1

plot 'c0129_gauss_fit_params.dat' u 2:($4*mm2microns):($6*mm2microns) t 'x' lt 2 with yerrorbars, \
	'c0129_gauss_fit_params.dat' u 3:($5*mm2microns):($6*mm2microns) t 'y' lt 1 w yerrorbars, \
	f1(x) lt 2 t 'f(x) = ax + b', \
	f2(x) lt 1 t 'f(x) = cx + d'