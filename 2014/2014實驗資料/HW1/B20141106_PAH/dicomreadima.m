clc;
clear all;
close all;

image1(:,:)=double(dicomread('B20141106_NTUST_PHATOM.MR.TYHUANG_KNIGHT.0017.0001.2014.11.06.11.54.16.996654.7882848.ima'));
        
%info = dicominfo(sprintf('B20141106_NTUST_PHATOM.MR.TYHUANG_KNIGHT.0013.0001.2014.11.06.11.54.16.996654.7873624.ima'));
        
% disp(x(ii).AcquisitionTime);
%aaa=str2num(info.AcquisitionTime);
figure(1),imshow(image1);
    