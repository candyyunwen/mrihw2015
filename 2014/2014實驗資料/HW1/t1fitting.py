# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 17:59:17 2014

@author: clark
"""

import dicom

import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
#import Image
from scipy.optimize.minpack import curve_fit

def plot(data, title):
    plot.i += 1
    plt.subplot(2,6,plot.i)
    plt.imshow(data)
    plt.gray()
    plt.title(title)
plot.i = 0



Acqtime = np.zeros(11)
Invtime = np.zeros(11)
Ttop = [0.12, 0.22, 0.37]



 

    
x = [20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000,2000]
print x
#y=[9.14492754,	18.01449275,28.26086957,39.0144927,49.4782608,60.62318841,71.3913043	, 82.72463768, 92.85507246,	193.1449275,286.0289855,376.0434783,460.4927536,538.3333333,611.9130435,680.1594203,745.1884058,805.2898551,1168.159 ]
#y=[10.4,23.2,36.1,48.8,61.0,73.4	,85.5,97.3,108.4,213.2,303.7,382.6	,449.3,506.3,555.6,595.1,630.3,660.3,779.7]
y=[4.5,9.4,14.0,18.6,23.1,	27.5,31.8,36.1,40.2,76.9,105.8,128.2,144.9,157.4,167.0,173.8,178.8,182.7,192.3]
#y=[27.8,54.9,81.1,106.3,130.7,154.6,177.9,200.3,221.8,405.5,535.4,626.1,688.2,731.2,761.2,778.3,792.6,802.9,821.7]
#y=[21.1,41.0,60.1,78.5,96.2,113.2,129.6,145.5,160.6,282.4,361.8,413.2,446.0,467.2,481.0,488.0,493.8,497.8,503.4]
#y=[5.6,10.7,15.7,20.4,24.9,29.4,33.5,37.6,41.3,71.2,88.8,98.9,104.9,108.0,109.7,110.4,110.8,111.2,111.1]

print y
smoothx = np.linspace(x[0], x[-1], 1000)



guess_a, guess_b = max(y), 200
guess = [guess_a, guess_b]
exp_f = lambda x, X0, T1:(X0*(1 - (np.exp(-x/T1))))

params, cov = curve_fit(exp_f, x, y, p0=guess)

X0, T1 = params

best_fit = lambda x: (X0*(1 - (np.exp(-x/T1))))

fitted_y=exp_f(smoothx, X0,  T1)






print X0

print T1

        


plt.figure(2)
plt.plot(x, y, 'o')

xxx = np.linspace(np.min(x), np.max(x), 1000)
plt.plot(xxx,exp_f(smoothx, X0,T1))