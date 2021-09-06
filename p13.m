%more filters

close all;
clear all;
clc;

a=double(imread("wb.jpg"));
figure;
imshow(uint8(a));

filter1=[-1 0 1; ...
         -1 0 1; ...
         -1 0 1];
b=imfilter(a,filter1); 
figure;
subplot(1,2,1);
imshow(uint8(b));

filter2=[1 0 -1; ...
         1 0 -1; ...
         1 0 -1];

c=imfilter(a,filter2);
subplot(1,2,2);
imshow(uint8(c));

