%Global Transformation on Images
close all;
clear all;
clc;

a=double(rgb2gray(imread('img1.bmp')));
figure;
subplot(1,2,1);
imshow(uint8(a));
title("Original Image in Grayscale", 'fontsize',15,'color',[240,24,245]/255);

%Log transformation
b=log(1+a);

%Normalization (manual)
m=min(min(b));
b=b-m;
M=max(max(b));
b=b/M;
b=b*256;

subplot(1,2,2);
imshow(uint8(b));
title("Transformed Image", 'fontsize',15,'color',[240,24,245]/255);



%Normalization (direct)
%subplot(1,2,2);
%imshow(b,[]);
%title("Transformed Image", 'fontsize',15,'color',[240,24,245]/255);

