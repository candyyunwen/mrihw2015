# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 17:59:17 2014

@author: clark
"""

import dicom

import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
import Image
from pylab import *
from scipy.optimize import curve_fit





Acqtime = np.zeros(11)
Invtime = np.zeros(11)




 

    
x = [20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000,2000]
print x
y = [9.14492754,	18.01449275,28.26086957,39.0144927,49.4782608,60.62318841,71.3913043	, 82.72463768, 92.85507246,	193.1449275,286.0289855,376.0434783,460.4927536,538.3333333,611.9130435,680.1594203,745.1884058,805.2898551,1168.159 ]

print y
















smoothx = np.linspace(x[0], x[-1], 1000)

def func(x, A,T1 ):
    return A*(1 - (np.exp(-x/T1)))

popt, pcov = curve_fit(func, x, y, [2000,50])
A, T1 = popt
print T1
print A

plt.figure(2)
plt.plot(x, y, 'o')

x = np.linspace(np.min(x), np.max(x), 1000)
plot(x,func(x,*popt))




        



