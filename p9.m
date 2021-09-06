%blurring fast, no loops

close all;
clear all;
clc;

a=double(rgb2gray(imread('img1.bmp')));
figure;
imshow(uint8(a));
title("Original");

%window
n=5; %size of window
filter=ones(n,n)/(n^2);

b=imfilter(a,filter);
figure;
imshow(uint8(b));
title("Blurred");

%sharps
c=a-b;
figure;
imshow(uint8(c));
title("Sharps");

%sharpened image
d=a+c;
figure;
imshow(uint8(d));
title("Sharpened Image");