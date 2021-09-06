%LOCAL TRANSFORMATION ON IMAGES
close all
clear all
clc

a=double(rgb2gray(imread('img1.bmp')));
figure
imshow(uint8(a))
title('INPUT IMAGE IN GRAYSCALE','fontsize',30,'color',[200,50,200]/255)

[r,c]=size(a);

win_size=3; % keep it odd
for i=(1+(win_size-1)/2):1:(r-(win_size-1)/2)
  for j=(1+(win_size-1)/2):1:(c-(win_size-1)/2)
    local_avg=mean(mean(   a((i-(win_size-1)/2):(i+(win_size-1)/2),(j-(win_size-1)/2):(j+(win_size-1)/2))   ));         
    if (local_avg<100) && (local_avg>30)
      a(i,j)=a(i,j)+100;
    end
  end
end

figure
imshow(uint8(a))
title('PROCESSED IMAGE','fontsize',30,'color',[200,50,200]/255);