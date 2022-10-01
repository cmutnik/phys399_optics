reset

set terminal png #transparent nocrop enhanced size 450,320 font "arial,8" 
set output 'gnuplot_contour.png'
set dummy u, v
set view 70, 20, 1, 1

 
#set key outside
#set cntrlabel  format '%8.3g' font ',7' start 5000 interval 200000
#set cntrparam levels auto 1000
#set style data lines
set pm3d
set contour #base
#set cntrparam levels incremental 0, 100, 200000

###
#set cntrparam cubicspline  # smooth out the lines
#set cntrparam levels 50    # sets the num of contour lines
#set pm3d interpolate 20,20 # interpolate the color
###




set dgrid3d 250,250
#set hidden3d
#set pm3d  at b
set samples 501, 501
set isosample 150,150


set ztics autofreq

set title "Sinc Function: c0129-0921 params" 
set xlabel "X Position" 
set ylabel "Y Position" 
set zlabel "Intensity" 

set xlabel  offset character -3, -2, 0 font "" textcolor lt -1 norotate
set ylabel  offset character 3, -2, 0 font "" textcolor lt -1 rotate by -270
set zlabel  offset character -5, 0, 0 font "" textcolor lt -1 rotate by 90

# get parameters from python code
Amp = 1710.16186871 # max height of intensity [pixels]
u0 = 328.019279141 # center x position [pixels]
v0 = 224.303943836 # y center position [pixels]
#uwidth = 99.957433021
#vwidth = 95.6489758889

set xrange [250:400]
set yrange [150:300]
#set xrange [ 0.0 : 640.0 ] noreverse nowriteback
#set yrange [ 0.0 : 640.0 ] noreverse nowriteback
set zrange [ -0.500000 : Amp ] noreverse nowriteback

sinc(u,v) = Amp*sin(sqrt((u-u0)**2+(v-v0)**2)) / sqrt((u-u0)**2+(v-v0)**2)
GPFUN_sinc = "sinc(u,v) = sin(sqrt(u**2+v**2)) / sqrt(u**2+v**2)"

x = 0.0
## Last datafile plotted: "$grid"
#splot [-12:12.01] [-12:12.01] sinc(u,v)
splot sinc(u,v) #w l