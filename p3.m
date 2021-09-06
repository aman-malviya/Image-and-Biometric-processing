%coloured to grayscale (averaging)

close all;
clear all;
clc;

a=imread('img1.bmp');
a=double(a);
figure;
imshow(uint8(a));

aR=a(:,:,1);
aG=a(:,:,2);
aB=a(:,:,3);

b=(aR+aG+aB)/3;

figure;
imshow(uint8(b));