%coloured to grayscale, predefined function rgb2gray

close all;
clear all;
clc;

a=double(rgb2gray(imread('img1.bmp')));
figure;
subplot(1,3,1);
imshow(uint8(a));

%inverting colors
a=255-a;
subplot(1,3,2);
imshow(uint8(a));

%blacking out a particular section
a(50:200, 50:200)=0;
subplot(1,3,3);
imshow(uint8(a));

