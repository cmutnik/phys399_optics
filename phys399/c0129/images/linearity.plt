set term png
set out 'sat_lin.png'
set fit errorvariables
set key off

set ylabel 'Saturation [counts]'
set xlabel 'ExpTime [s]'
set title 'Saturation Linearity'

f1(x) = a*x + b
a = 1;
b = 1;
fit f1(x) 'c0129_linearity_params3.dat' u 6:1 via a,b

#set label 1 sprintf("X^2 = %3.5g",FIT_STDFIT**2) at 0.075,3500 font "arialbd,15" tc lt 2
set label 1 sprintf("f(x) = %3.5gx%3.5g",a,b) at 0.075,3500 font "arialbd,15" tc lt 3


plot 'c0129_linearity_params3.dat' u 6:1 lt 3, \
	f1(x) lt 3