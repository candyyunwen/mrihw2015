# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 15:36:35 2015

@author: MRI_Yun
"""

import dicom

import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
from pylab import *
from scipy.optimize import curve_fit
im = np.zeros((16,256,256))   #把圖存在3維距陣裡
te = np.zeros((16))
x = []
y = []

#ds = dicom.read_file('TR_1.ima')
#image = ds.pixel_array 
#print ds
#print image
        
for i in range(16):
    im[i] = (dicom.read_file("TE_%d.ima"%(i+1))).pixel_array  
    te[i] = (dicom.read_file("TE_%d.ima"%(i+1))).EchoTime
    x.append(te[i])
    y.append(im[i][128][128])

def func(x, X0,T2):
    return X0*(np.exp(-x/T2))

popt, pcov = curve_fit(func, x, y, [2000,50])
X0, T2 = popt
print ("T2 = %f, X0 = %f" %(T2,X0))

plt.figure()
plt.plot(x, y, 'o')

x = np.linspace(np.min(x), np.max(x), 1000)
plt.ylim(0,1000)
plot(x,func(x,*popt))    

'''
#畫出火龍果
plt.figure()
plt.imshow(im[8], cmap=plt.cm.gray)
plt.colorbar()
'''