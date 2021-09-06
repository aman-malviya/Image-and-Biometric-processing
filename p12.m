%Ideal filter and smooth decay filter

close all;
clear all;
clc;

a=double(rgb2gray(imread("img1.bmp")));
figure;
imshow(uint8(a));

%ideal filter (the one we have used before)
n=5;
filter1=ones(n,n)/(n^2);
b=imfilter(a,filter1);
subplot(1,2,1);
imshow(uint8(b));


%smooth decay filter
filter2=[0 0 1 0 0; ...
         0 1 2 1 0; ...
         1 2 4 2 1; ...
         0 1 2 1 0; ...
         0 0 1 0 0;];  
filter2=filter2/sum(sum(filter2));
c=imfilter(a,filter2);
subplot(1,2,2);
imshow(uint8(c));