# Basics of matplotlib

import numpy as np
import matplotlib.pyplot as plt

Fs=1000
T=1/Fs
L=1001
t=np.linspace(0,L-1,L)*T

f1=5
sig1=np.sin(2*np.pi*f1*t)
f2=2
sig2=np.cos(2*np.pi*f2*t)
sig3=t.copy()

fig1,ax1=plt.subplots()
fig1.show()
plt.plot(t,sig1,label="Sine Curve", color="g", marker=".")
plt.plot(t,sig2,label="Cosine Curve", color="r",marker=".")
plt.plot(t,sig3,label="Line",linestyle="dashed",linewidth=3)
plt.grid()
plt.title("My first python plot", fontsize=20)
plt.xlabel("Time Axis")
plt.ylabel("Amplitude")
plt.legend()
plt.show()

sig4=np.array([1,2,3,4,5,6,7,8,9,15,1,8,1,6,1,4,4,5,11,55,7,84,5,96,4])
sig5=sig4[::-1]
x=np.linspace(0,24,25)
fig2,ax2=plt.subplots()
fig2.show()
ax2.stem(x,sig4,label="Signal 4")
ax2.stem(x,sig5,label="Signal 5",linefmt="--")
plt.grid()
ax2.set_title("Signal 4 and Signal 5")
ax2.set_xlabel("X axis")
ax2.set_ylabel("Y axis")
plt.legend()
plt.show()