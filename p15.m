% Learning SOBEL operator for derivative of image
% Learning Gradient

close all
clear all
clc

pkg load image

a=double(rgb2gray(imread('img1.jpg')));
figure
imshow(uint8(a));
title('Original Image','fontsize',20)

[r c]=size(a);

% Filters
filter1=[-1 0 1; ...
         -2 0 2; ...
         -1 0 1;];
         
filter2=[ 1  2  1; ...
          0  0  0; ...
         -1 -2 -1;];



bx=imfilter(a,filter1); 
figure
imshow(bx,[]);
title('SOBEL (x direction)','fontsize',20);

by=imfilter(a,filter2); 
figure
imshow(by,[]);
title('SOBEL (y direction)','fontsize',20);

Grad_mag=(bx.^2+by.^2).^(1/2);
figure
imshow(Grad_mag,[]);
title('GRADIENT MAGNITUDE','fontsize',20);