%disintegrating rgb frames (each of these frames will have intensities in the form of shades of grey)

close all;
clear all;
clc;

a=imread('rgb.bmp');
figure;
imshow(a);

aR=a(:,:,1);
aG=a(:,:,2);
aB=a(:,:,3);

figure;
subplot(1,3,1);
imshow(aR);
title("Red Frame");

subplot(1,3,2);
imshow(aG);
title("Green Frame");

subplot(1,3,3);
imshow(aB);
title("Blue Frame");
