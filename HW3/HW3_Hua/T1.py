# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 14:47:52 2015

@author: MRI-Handsome
"""

import dicom

import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
from pylab import *
from scipy.optimize import curve_fit


#y1=[]
x=[]
a = np.zeros((9)) 
b = np.zeros((256,256,9)) 
c = np.zeros((256,256)) 
im = np.zeros((9,256,256))   #把圖存在3維距陣裡
tr = np.zeros((9)) 


def func(x, A,T1 ):
    return A*(1 - (np.exp(-x/T1)))
    
    
for i in range(9): 
        im[i] = (dicom.read_file("%d.ima"%(i+1))).pixel_array
        tr[i] = (dicom.read_file("%d.ima"%(i+1))).RepetitionTime
        x.append(tr[i])

for j in range(256):
    for k in range(256): 
        for i in range(9):    #  九章像素值當作縱軸
            b[j][k][i] = im[i][j][k]
        a=b[j][k]
        popt, pcov = curve_fit(func, x, a, [2000,100])
        A, T1 = popt  
        if T1>5000:
           T1=100
           c[j][k] = T1
        else :
            c[j][k] = T1
        
        
            




#  劃出火龍果
plt.figure()
plt.imshow(c, cmap=plt.cm.gray)
plt.colorbar()


#劃出T1的公式


popt, pcov = curve_fit(func, x, b[140][140], [2000,100])
A, T1 = popt


plt.figure(2)
plt.plot(x, b[140][140], 'o')

x = np.linspace(np.min(x), np.max(x), 1000)
plot(x,func(x,*popt))

