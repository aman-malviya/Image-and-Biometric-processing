import numpy as np
import matplotlib.pyplot as plt

x=np.array([1,1,0,3])
h=np.array([2,3,1,1])

y=np.convolve(x,h)

fig = plt.figure()
ax1 = fig.add_subplot(221)
ax3 = fig.add_subplot(122)
ax2 = fig.add_subplot(223)

plt.subplots_adjust(wspace=0.3,hspace=0.3)

ax1.stem(x)
ax1.set_xlabel("N")
ax1.set_ylabel("Amplitude")
ax1.set_title("Input Sequence X")

ax2.stem(h)
ax2.set_xlabel("N")
ax2.set_ylabel("Amplitude")
ax2.set_title("Input Sequence H")

ax3.stem(y)
ax3.set_xlabel("N")
ax3.set_ylabel("Amplitude")
ax3.set_title("Output Sequence Y")

plt.show()
