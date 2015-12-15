# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 23:15:53 2015

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
a = np.zeros((16)) 
b = np.zeros((256,256,16)) 
c = np.zeros((256,256)) 
im = np.zeros((16,256,256))   #把圖存在3維距陣裡
te = np.zeros((16)) 
   


for i in range(16): 
        im[i] = (dicom.read_file("%d.ima"%(i+10))).pixel_array
        te[i] = (dicom.read_file("%d.ima"%(i+10))).EchoTime
        x.append(te[i])
        
smoothx = np.linspace(x[0], x[-1], 1000)

#image = ds.pixel_array

for j in range(256):
    for k in range(256): 
        for i in range(16):    #  九章像素值當作縱軸
            b[j][k][i] = im[i][j][k]
        a=b[j][k]
        
        

        guess_a, guess_b = max(a), 200
        guess = [guess_a, guess_b]


        exp_f = lambda x, X0, T2:(X0*(np.exp(-x/T2)))

        params, cov = curve_fit(exp_f, x, a, p0=guess)

        X0, T2 = params

        best_fit = lambda x: (X0*(np.exp(-x/T2)))

        fitted_y=exp_f(smoothx, X0,  T2)  

        c[j][k] = T2
        if c[j][k]>100:
            c[j][k]=0
        elif 90<c[j][k]<100:
            c[j][k]=1000
    
        elif 80<c[j][k]<90:
            c[j][k]=900

        elif 70<c[j][k]<80:
            c[j][k]=800

        elif 60<c[j][k]<70:
            c[j][k]=700

        elif 50<c[j][k]<60:
            c[j][k]=600

        elif 40<c[j][k]<50:
            c[j][k]=500

        elif 30<c[j][k]<40:
            c[j][k]=400

        elif 20<c[j][k]<30:
            c[j][k]=300
        elif 10<c[j][k]<20:
            c[j][k]=200
        else :
            c[j][k]=100
          
          
        
    
        
            




#  劃出火龍果
plt.figure()
plt.imshow(c, cmap=plt.cm.gray)
plt.colorbar()


#劃出T1的公式

guess_a, guess_b = max(b[140][140]), 200
guess = [guess_a, guess_b]


exp_f = lambda x, X0, T2:(X0*(np.exp(-x/T2)))

params, cov = curve_fit(exp_f, x, b[140][140], p0=guess)

X0, T2 = params

best_fit = lambda x: (X0*(np.exp(-x/T2)))

fitted_y=exp_f(smoothx, X0,  T2)  





plt.figure(2)
plt.plot(x, b[140][140], 'o')

x = np.linspace(np.min(x), np.max(x), 1000)
plot(x,fitted_y)

