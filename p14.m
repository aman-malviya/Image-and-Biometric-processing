% Learning Point detector

close all
clear all
clc

pkg load image

a=double(rgb2gray(imread('img2.bmp')));
figure
imshow(uint8(a));
title('Original Image','fontsize',20)

[r c]=size(a);
b=zeros(r,c);

% Filters
filter1=[-1 -1 -1; ...
         -1  8 -1; ...
         -1 -1 -1;];

b=imfilter(a,filter1); 

b=b-min(min(b));
b=255*(b/max(max(b)));
figure
imshow(uint8(b));
title('Filtered NORMALISED Image','fontsize',20);







