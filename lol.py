from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def FresnelS(t):
    return .626 - .5*((np.cos(t**2)/t) + .5*(np.sin(t**2)/t**3))

def FresnelC(t):
    return .626 + .5*((np.sin(t**2)/t) - .5*(np.cos(t**2)/t**3))

t = np.linspace(.00001,1000,100000)

v = 73.56 +13.94+ 17.82*FresnelC(.0063*t + 3.16) - 158*FresnelS(.0063*t + 3.16) 

plt.plot(t,v)
#print np.mean(v[3:])

##plt.plot(x,v,'o')

#x = np.array([63.5, 189.6, 295.9, 389.7, 474.45, 552.45, 625.05, 693.22])
#y = np.array([v[6350],v[18960],v[29590],v[38970],v[47445],v[55245],v[62505],v[69322]])
#logy = np.log(y)

#def fit(x,m,c):
    #return m*x + c

#p,pcov = curve_fit(fit,x,logy)

#logfit = fit(x,p[0],p[1])
#print p[0]
#plt.plot(x,logy,'o')
#plt.plot(x,logfit)
plt.show()