import matplotlib.pyplot as plt
import numpy as np
from time import sleep

fs=1000
T=1/fs
a=np.sin(2*np.pi*5*T)

fig1,ax1=plt.subplots()
ax1.plot(T,a)
fig1.show()
sleep(60)