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
from scipy.optimize.minpack import curve_fit

def plot(data, title):
    plot.i += 1
    plt.subplot(2,6,plot.i)
    plt.imshow(data)
    plt.gray()
    plt.title(title)
plot.i = 0


im = np.zeros((256,208))
T1im = np.zeros((256,208))
Acqtime = np.zeros(11)
Invtime = np.zeros(11)
Ttop = [0.12, 0.22, 0.37]
Tx = np.zeros(11)

i=1


'''
#read image
for i in range(11): 
    im[i] = (dicom.read_file("BH00%d.dcm"%(i+1))).pixel_array
    Acqtime[i] = float((dicom.read_file("BH00%d.dcm"%(i+1))).AcquisitionTime)
    Invtime[i] = (dicom.read_file("BH00%d.dcm"%(i+1))).InversionTime    
    plot(im[i], 'image%d'%i)
'''



filename = 'TR3000_TE434'

im = (dicom.read_file("%s.ima"%(filename))).pixel_array
#im2 = (dicom.read_file("TR500_TE12_2.ima")).pixel_array

print 'TR:', (dicom.read_file("%s.ima"%(filename))).RepetitionTime
print 'TE:', (dicom.read_file("%s.ima"%(filename))).EchoTime



plt.gray()
plt.figure(1)
plt.imshow(im)

#plt.figure(2)
#plt.imshow(im2)

#圈選的位置(40,15)(89,17)(37,64)(90,65)(39,115)(87,116)半徑=5
x1=40
y1=15
x2=38
y2=65
x3=40
y3=115
x4=89
y4=17
x5=90
y5=65
x6=88
y6=116
n= np.zeros(6)
sn= np.zeros(6)
sav = np.zeros(6)


for ii in range( 0 , 128 ):  
    for jj in range( 0 , 128 ): 
        if((((ii-y1)**2+(jj-x1)**2)**0.5)<5):
            n[0]+=1            
            sn[0]=sn[0]+im[ii,jj]
            sav[0] = sn[0]/n[0]    
        if(((((ii-y1)**2+(jj-x1)**2)**0.5)>=5)and((((ii-y1)**2+(jj-x1)**2)**0.5)<6)):
            im[ii,jj]=5000           
            
        if((((ii-y2)**2+(jj-x2)**2)**0.5)<5):
            n[1]+=1            
            sn[1]=sn[1]+im[ii,jj]
            sav[1] = sn[1]/n[1]
        if(((((ii-y2)**2+(jj-x2)**2)**0.5)>=5)and((((ii-y2)**2+(jj-x2)**2)**0.5)<6)):
            im[ii,jj]=5000   
            
        if((((ii-y3)**2+(jj-x3)**2)**0.5)<5):
            n[2]+=1            
            sn[2]=sn[2]+im[ii,jj]
            sav[2] = sn[2]/n[2]
        if(((((ii-y3)**2+(jj-x3)**2)**0.5)>=5)and((((ii-y3)**2+(jj-x3)**2)**0.5)<6)):
            im[ii,jj]=5000     
            
        if((((ii-y4)**2+(jj-x4)**2)**0.5)<5):
            n[3]+=1            
            sn[3]=sn[3]+im[ii,jj]
            sav[3] = sn[3]/n[3]
        if(((((ii-y4)**2+(jj-x4)**2)**0.5)>=5)and((((ii-y4)**2+(jj-x4)**2)**0.5)<6)):
            im[ii,jj]=5000                
            
        if((((ii-y5)**2+(jj-x5)**2)**0.5)<5):
            n[4]+=1            
            sn[4]=sn[4]+im[ii,jj]
            sav[4] = sn[4]/n[4]
        if(((((ii-y5)**2+(jj-x5)**2)**0.5)>=5)and((((ii-y5)**2+(jj-x5)**2)**0.5)<6)):
            im[ii,jj]=5000     
            
        if((((ii-y6)**2+(jj-x6)**2)**0.5)<5):
            n[5]+=1            
            sn[5]=sn[5]+im[ii,jj]
            sav[5] = sn[5]/n[5]
        if(((((ii-y6)**2+(jj-x6)**2)**0.5)>=5)and((((ii-y6)**2+(jj-x6)**2)**0.5)<6)):
            im[ii,jj]=5000     

print sav


























