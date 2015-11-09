clear all
close all
clc
x = 1; %Mz(0)
m = 1; %M0
angle = 25.; %flip angle
t = 0.1; %TR/T2
j=1;
k=1;

for i= 1:100
    if(i ==1)
       x = 1;
       fprintf ('Mz: %f , Mz^: %f , Mxy: %f  \n' , x, x*cos(angle/180*pi), x*sin(angle/180*pi))  
       a(i) = x;
       c(j) = a(i);
       j = j+1;
       b(i) = x*cos(angle/180*pi) ;
       c(j) = b(i);
       j = j+1;     
    else
        x = (x*cos(angle/180*pi)*exp(-t))+m*(1-exp(-t));
        fprintf ('Mz: %f , Mz^: %f , Mxy: %f  \n' , x, x*cos(angle/180*pi), x*sin(angle/180*pi))
        a(i) = x;
        c(j) = a(i);
        j = j+1;
        b(i) = x*cos(angle/180*pi) ;
        c(j) = b(i);
        j = j+1;
    end 
end
for i = 1:99
    if(i ==1)
        d(i) = 0;
        f(k) = d(i);
        k = k+1;
        e(i) = 0;
        f(k) = e(i);
        k = k+1;  
    end
    d(i) = i/10;
    f(k) = d(i);
    k = k+1;
    e(i) = i/10;
    f(k) = e(i);
    k = k+1;
end

plot(f,c)
grid on
