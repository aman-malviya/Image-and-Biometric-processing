#Making multiple plots in same figure

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

sig4=np.array([1,2,3,4,5,6,7,8,9,15,1,8,1,6,1,4,4,5,11,55,7,84,5,96,4])
sig5=sig4[::-1]
x=np.linspace(0,24,25)

fig1,ax1=plt.subplots(2,3)
fig1.show()
ax1[0,0].plot(t,sig1)
ax1[0,1].plot(t,sig2)
ax1[0,2].plot(t,sig3)
ax1[1,0].plot(x,sig4)
ax1[1,1].plot(x,sig5)
plt.show()

