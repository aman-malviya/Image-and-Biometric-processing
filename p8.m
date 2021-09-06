% Learning Filtering in SPATIAL DOMAIN (LOOP METHOD - SLOW)
%Blurring, inverting, Sharpening
close all
clear all
clc

a=double(rgb2gray(imread('img1.bmp')));
figure(100);
imshow(uint8(a));
title('Original Image','fontsize',20,'color',[255 0 0]/255)

[r c]=size(a);
b=zeros(r,c);

n=5; %should be odd
for i=(1+(n-1)/2):1:(r-(n-1)/2)
    for j=(1+(n-1)/2):1:(c-(n-1)/2)
        b(i,j)=mean2(a((i-(n-1)/2):(i+(n-1)/2),(j-(n-1)/2):(j+(n-1)/2)));
    end
end
    
figure (50)
imshow(uint8(b));
title('Blurred Image','fontsize',20,'color',[0 255 0]/255);

c=a-b;
figure(1)
imshow(uint8(c))
title('Difference Image','fontsize',20,'color',[255 127 39]/255);

d=a+c;
figure(2)
imshow(uint8(d))
title('Sharpened Image','fontsize',20,'color',[255 127 39]/255);