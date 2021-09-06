%histogram using imhist

close all;
clear all;
clc;

a=rgb2gray(imread("img1.bmp"));
figure;
subplot(1,2,1);
imshow(a);

subplot(1,2,2);
imhist(a);
title("Default 256 bin histogram");

%imhist features
figure;
subplot(1,2,1);
imhist(a,10);
title("10 bin histogram");

subplot(1,2,2);
imhist(a,20);
title("20 bin histogram");
