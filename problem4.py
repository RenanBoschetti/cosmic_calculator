import numpy as np
import scipy.integrate as integrate
import matplotlib
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
matplotlib.use('Agg')
import matplotlib.pyplot as pl
from scipy.interpolate import interp1d

Om = 0.3158
Or =  2* 10**(-5)
Ol = 1 - (Om + Or)
H0 = 0.0736  # in units of 1/Gy 
c = (3*10**8) * (3.24*10**-5)/3.17 # in units of Mpc/Gy 
z = 10

# Hubble function in units of H0
def E(z): 
	return np.sqrt(Om*(1.+z)**(3.) + Ol + Or*(1.+z)**4.)

t0 = 1./H0 # in units of Gy

# The cosmic time at redshift z in units of H0
def I(z):
	return integrate.quad(lambda zv: ( 1./(1.+zv) ) * (1./E(zv) ), z, 0 )[0]

# The cosmic time 
def Dt(z):
	return I(z)/H0 + t0	

print (" The cosmic time at z = "+ np.str(z)+ " is "  + np.str(np.round(Dt(z), 2)) + " Gy. The age of Universe is " + np.str(np.round(1/H0, 2))+" Gy. That is, the light of a galaxy at z = " + np.str(z) + " was emmited when the Universe had " + np.str(np.round(Dt(z)/(1/H0), 2))  + " of its current age.")	

zvec = np.arange(1000., 0., -0.1)
tvec = np.ones(len(zvec))

for i in range(len(tvec)):
	tvec[i] = Dt(zvec[i])

z_fun_t = interp1d(tvec, zvec, kind = 'cubic')	

# Plot z x t 
pl.figure()
pl.loglog(tvec, zvec, color ='black')
pl.grid(True)
pl.xlabel(r"t [Gy]", fontsize = 20, usetex = True)
pl.ylabel(r"z(t)  ", fontsize = 20, usetex = True)
pl.xlim(0., 14.)
pl.ylim(0., 10)
pl.savefig('t_z_log.png')


pl.figure()
pl.plot(tvec, zvec, color ='black')
pl.grid(True)
pl.xlabel(r"t [Gy]", fontsize = 20, usetex = True)
pl.ylabel(r"z(t)", fontsize = 20 , usetex = True)
pl.xlim(0., 14.)
pl.ylim(0., 10)
pl.savefig('t_z.png')

