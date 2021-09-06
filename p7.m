%Functions in matlab

close all;
clear all;
clc;

function [s]=sum(a,b)
  s=a+b;
end;

a=3;
b=5;
c=sum(a,b);

d=multiply(a,b);  %function in separate file
[c d] %print to command line