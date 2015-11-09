clear all
clc
O=input('角度=');
T=input('tr/t1=');
k1=1;
k2=1;
c=1;
i=2;
j=2;
for n=0:1:40 ;
    a(k1)=c*cosd(O)*exp(-T)+1*(1-exp(-T));
    m1(i)=a(k1);
    x(j)=k1;
    i=i+1;
    j=j+1;
    b(k2)=c*cosd(O)*exp(-T);
    m1(i)=b(k2);
    x(j)=k2;
    i=i+1;
    j=j+1;
    c=a(k1);
    k1=k1+1;
    k2=k2+1;
    
end
m1(1)=cosd(O)*exp(-T);         %起始點值
n=0:1:40;
Mx=c*sind(O)                   %算出Mxy穩定植
 subplot(2,2,1),plot(x,m1,'r');
 xlabel('時間');
 ylabel('MZ');
 legend('M1');
 
%clear all
%clc
O=input('角度=');
T=input('tr/t1=');
k1=1;
k2=1;
c=1;
i=2;
j=2;
for n=0:1:40 ;
    a(k1)=c*cosd(O)*exp(-T)+1*(1-exp(-T));
    m2(i)=a(k1);
    x(j)=k1;
    i=i+1;
    j=j+1;
    b(k2)=c*cosd(O)*exp(-T);
    m2(i)=b(k2);
    x(j)=k2;
    i=i+1;
    j=j+1;
    c=a(k1);
    k1=k1+1;
    k2=k2+1;
    
end
m2(1)=cosd(O)*exp(-T);
n=0:1:40;
%x(0)=cosd(O)*exp(-T);
Mx=c*sind(O)
 subplot(2,2,2),plot(x,m2);
 xlabel('時間');
 ylabel('MZ');
 legend('M2');
 
%clear all
%clc
O=input('角度=');
T=input('tr/t1=');
k1=1;
k2=1;
c=1;
i=2;
j=2;
for n=0:1:40 ;
    a(k1)=c*cosd(O)*exp(-T)+1*(1-exp(-T));
    m3(i)=a(k1);
    x(j)=k1;
    i=i+1;
    j=j+1;
    b(k2)=c*cosd(O)*exp(-T);
    m3(i)=b(k2);
    x(j)=k2;
    i=i+1;
    j=j+1;
    c=a(k1);
    k1=k1+1;
    k2=k2+1;
    
end
m3(1)=cosd(O)*exp(-T);
n=0:1:40;
%x(0)=cosd(O)*exp(-T);
Mx=c*sind(O)
 subplot(2,2,3),plot(x,m3,'g');
 xlabel('時間');
 ylabel('MZ');
 legend('M3');
 
 subplot(2,2,4),plot(x,m1,'r',x,m2,'b',x,m3,'g');
 xlabel('時間');
 ylabel('MZ');
 title('比較圖');
 legend('M1','M2','M3');