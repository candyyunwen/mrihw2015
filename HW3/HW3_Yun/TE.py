# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 15:42:44 2015

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
a = []
b = []
T2_map = np.zeros((256,256))
q = 0
r = 0
p = 0
for i in range(16):
    im[i] = (dicom.read_file("TE_%d.ima"%(i+1))).pixel_array #pixel
    te[i] = (dicom.read_file("TE_%d.ima"%(i+1))).EchoTime #TR

for m in range(256):
    for n in range(256):
        for i in range(16):
            a.append(te[i])
            b.append(im[i][m][n])
        x = a[p:p+16]          
        y = b[p:p+16]
        
        def func(x, X0, T2):
            return X0*(np.exp(-x/T2))
    
        popt, pcov = curve_fit(func, x, y, [2000,50])
        X0, T2 = popt
#        print ("T2 = %f, X0 = %f" %(T2,X0))
    
        if(p%16==0):
            if(T2 > 100):
                T2 = 0
            if(T2 < 0):
                T2 = 100
            T2_map[q][r] = T2
            r = r+1
            if(r>255):
                q = q+1
                r = 0
        p = p+16
        

        #畫出全部的圖    
        figure = plt.figure(figsize=[15,5])
        plt.subplot(121)
        plt.plot(x, y, 'o')
        x = np.linspace(np.min(x), np.max(x), 1000)
        plt.ylim(0,1000)
        plt.plot(x,func(x,*popt))  

        plt.subplot(122)
        plt.imshow(T2_map, cmap=plt.cm.gray)
        plt.xlim(0,256)
        plt.ylim(256,0)
        plt.savefig("TE_fig%d.jpg"%(p/16))

'''
#畫出T2_map
plt.figure(figsize=[15,5])
plt.subplot(121)
plt.imshow(T2_map)
plt.colorbar() 
plt.subplot(122)
plt.imshow(T2_map, cmap=plt.cm.gray)
plt.colorbar() 
plt.savefig("TE_map.jpg")
'''