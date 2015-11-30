# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 15:25:27 2015

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
a = []
b = []
T1_map = np.zeros((256,256))
q = 0
r = 0
p = 0
for i in range(9):
    im[i] = (dicom.read_file("TR_%d.ima"%(i+1))).pixel_array #pixel
    tr[i] = (dicom.read_file("TR_%d.ima"%(i+1))).RepetitionTime #TR

for m in range(256):
    for n in range(256):
        for i in range(9):
            a.append(tr[i])
            b.append(im[i][m][n])
        x = a[p:p+9]          
        y = b[p:p+9]
        
        def func(x, X0,T1 ):
            return X0*(1 - (np.exp(-x/T1)))
    
        popt, pcov = curve_fit(func, x, y, [2000,50])
        X0, T1 = popt
#        print ("T1 = %f, X0 = %f" %(T1,X0))
    
        if(p%9==0):
            if(T1 > 5000):
                T1 = 5000
            T1_map[q][r] = T1
            r = r+1
            if(r>255):
                q = q+1
                r = 0
        p = p+9
        
 '''   
        #畫出全部的圖
        plt.figure(figsize=[15,5])
        plt.subplot(121)
        plt.plot(x, y, 'o')
        x = np.linspace(np.min(x), np.max(x), 1000)
        plt.ylim(0,1000)
        plt.plot(x,func(x,*popt))  

        plt.subplot(122)
        plt.imshow(T1_map, cmap=plt.cm.gray)
        plt.xlim(0,256)
        plt.ylim(256,0)
        plt.savefig("TR_fig%d.jpg"%(p/9))

'''
#畫出T1_map
plt.figure(figsize=[15,5])
plt.subplot(121)
plt.imshow(T1_map)
plt.colorbar() 
plt.subplot(122)
plt.imshow(T1_map, cmap=plt.cm.gray)
plt.colorbar() 
plt.savefig("TR_map.jpg")
