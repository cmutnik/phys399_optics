c = 299792458 #[m/s]
n_bk7 = 1.511
n_air = 1.
#n_air = 1.00029
theta_air = 45. #[deg]


deg2rad = np.pi/180.

theta1 = theta_air*deg2rad
theta2 = np.arcsin(np.sin(theta1)*n_air/n_bk7) #[rad]
theta2deg = theta2*(180./np.pi) #[deg]
theta2deg

phi = theta_air - theta2

d = 0.00343 #[m] = 3.43[mm]

Lp = d/(np.cos(theta2))
#Lp = d/np.cos(phi*deg2rad)


v_ax = 1090. #[MHz]

RHS = 1./v_ax


#LHS1 = (2.*(L1+L2)*n_air)/c

LHS2 = 2.*Lp*n_bk7/c

#((1/1090MHz)*(speed of light)/(2.*1.000)) - (3.9123881432034263e-11seconds*(speed of light)/(2.*1.000))
#0.1317 m
L1L2 = ((1./v_ax)*c/(2.*n_air)) - (Lp*n_bk7/n_air) # = L1 + L2
#>>137479.62580389174



#WOLFRAM >> 0.1321m
#[1/1090MHz] - [2*1.511*(3.43mm)/(cos(27.91deg)*299792458meters per second] 
#>>8.783×10^-10 seconds
#299792458meters per second*8.783×10^-10 seconds/(2*1.00029)
#>> 0.1316m
xx = c * v_ax / (2.*n_air)



###
#with n_air = 1
#[1/1090MHz] - [2*1.511*(3.43mm)/(cos(45deg-27.902781730050982deg)*299792458meters per second] 
testy = (v_ax*c/2.*n_air) - (2.*n_bk7*d / (np.cos(phi*deg2rad)*c))/(2.*n_air)


