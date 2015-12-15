# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 14:02:11 2015

@author: MRI_Yun
"""

import dicom

import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
from pylab import *
from scipy.optimize import curve_fit
im = np.zeros((9,256,256))   #把圖存在3維距陣裡
tr = np.zeros((9))
x = []
y = []

#ds = dicom.read_file('TR_1.ima')
#image = ds.pixel_array 
#print ds
#print image
        
for i in range(9):
    im[i] = (dicom.read_file("TR_%d.ima"%(i+1))).pixel_array  
    tr[i] = (dicom.read_file("TR_%d.ima"%(i+1))).RepetitionTime
    x.append(tr[i])
    y.append(im[i][128][128])

def func(x, X0,T1 ):
    return X0*(1 - (np.exp(-x/T1)))

popt, pcov = curve_fit(func, x, y, [2000,50])
X0, T1 = popt
print ("T1 = %f, X0 = %f" %(T1,X0))

plt.figure()
plt.plot(x, y, 'o')

x = np.linspace(np.min(x), np.max(x), 1000)
plt.ylim(0,1000)
plot(x,func(x,*popt)) 


'''
#畫出火龍果
plt.figure()
plt.imshow(im[5], cmap=plt.cm.gray)
plt.colorbar()
'''
