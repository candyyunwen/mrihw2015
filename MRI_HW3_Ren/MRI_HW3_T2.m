clc
clear all
P10=dicomread('10.IMA');
P11=dicomread('11.IMA');
P12=dicomread('12.IMA');
P13=dicomread('13.IMA');
P14=dicomread('14.IMA');
P15=dicomread('15.IMA');
P16=dicomread('16.IMA');
P17=dicomread('17.IMA');
P18=dicomread('18.IMA');
P19=dicomread('19.IMA');
P20=dicomread('20.IMA');
P21=dicomread('21.IMA');
P22=dicomread('22.IMA');
P23=dicomread('23.IMA');
P24=dicomread('24.IMA');
P25=dicomread('25.IMA');
K10=P10';
K11=P11';
K12=P12';
K13=P13';
K14=P14';
K15=P15';
K16=P16';
K17=P17';
K18=P18';
K19=P19';
K20=P20';
K21=P21';
K22=P22';
K23=P23';
K24=P24';
K25=P25';
ti=[16.1 32.2 48.3 64.4 80.5 96.6 112.7 128.8 144.9 161 177.1 193.2 209.3 225.4 241.5 257.6];
guess = [0 500];
f=@(guess,ti)guess(1).*(exp(-ti./guess(2)));
for  i=1:65536;
m2=[double(K10(i)) double(K11(i)) double(K12(i)) double(K13(i)) double(K14(i)) double(K15(i)) double(K16(i)) double(K17(i)) double(K18(i)) double(K19(i)) double(K20(i)) double(K21(i)) double(K22(i)) double(K23(i)) double(K24(i)) double(K25(i))];
 Mz=lsqcurvefit(f,guess,ti,m2);
T2(i)=Mz(2);
  i=i+1;
end
for j=1:256;
    P2(j,1:256)=T2(256*j-255:256*j)
    j=j+1;
end
imshow(P2,[])