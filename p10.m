%making an histogram (using loops, brute force)

x=[1:1:256];
y=x;

a=rgb2gray(imread("img1.bmp"));

[r c]=size(a);

for i=1:1:r
  for j=1:1:c
    [r c];
    y(a(i,j)+1)+=1;
  end
end

figure;
histo=stem(x,y,'Marker','none');
grid on;
xlabel("Intensity", 'fontsize',20);
ylabel("Number of Pixels (Frequency)", 'fontsize',20);
title("Histogram", 'fontsize',30);