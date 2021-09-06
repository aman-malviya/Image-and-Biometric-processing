%Basics of plot

t=0:.001:3;
a=sin(2*pi*5*t);
figure;
plot(t,a);
a=sin(2*pi*t);
plot(t,a);
xlabel("Time");
xlabel("Time", 'fontsize', 20);
ylabel("Amplitude", 'fontsize', 20);
title("My Plot", 'fontsize', 30);
grid on;
hold on;
b=cos(2*pi*t);
plot(t,b,'m');
legend("Sine", "Cosine");
hold off;