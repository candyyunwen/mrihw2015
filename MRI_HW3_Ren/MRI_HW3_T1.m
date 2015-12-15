clc
clear all
P1=dicomread('1.IMA');%讀取T1影像資料
P2=dicomread('2.IMA');
P3=dicomread('3.IMA');
P4=dicomread('4.IMA');
P5=dicomread('5.IMA');
P6=dicomread('6.IMA');
P7=dicomread('7.IMA');
P8=dicomread('8.IMA');
P9=dicomread('9.IMA');
K1=P1';               %做轉置
K2=P2';
K3=P3';
K4=P4';
K5=P5';
K6=P6';
K7=P7';
K8=P8';
K9=P9';
ti=[100 200 300 400 500 600 800 1000 1500];                                 %設定ti時間
guess = [0 5000];
f=@(guess,ti)guess(1).*(1-exp(-ti./guess(2)));                              %定義T1 fitting公式
for  i=1:65536;
 m=[double(K1(i)) double(K2(i)) double(K3(i)) double(K4(i)) double(K5(i))   %分別取出每張圖片每一點的值做運算
     double(K6(i)) double(K7(i)) double(K8(i)) double(K9(i))];
 Mz=lsqcurvefit(f,guess,ti,m);                                              %T1 fitting
 T1(i)=Mz(2);
  i=i+1;
end
for j=1:256;                                                                %將陣列轉成矩陣
    P(j,1:256)=T1(256*j-255:256*j)
    j=j+1;
end
imshow(P,[])