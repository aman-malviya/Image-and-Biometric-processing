# Blurring in frequency domain
# Low pass filter
# Gibbs Phenomenon (Ideal filter)

import numpy as np
import matplotlib.pyplot as plt
import cv2
from utils import Figure,TF

# Original Image
fig = Figure(2,3)
a = np.float32(cv2.imread('./img1.bmp', 0))
fig.plot_for_me(1,np.uint8(a))

# Fourier Transform (space to frequency domain)
b = np.fft.fftshift(np.fft.fft2(a))
fig.plot_for_me(2,np.uint8(TF.normalize(TF.log(b))))


# Filter
r = len(a)
c = len(a[0])
filter1 = np.zeros((r, c))
radius = 30
for i in range(r):
    for j in range(c):
        if np.sqrt((i-r/2)**2+(j-c/2)**2) < radius:
            filter1[i][j] = 1
fig.plot_for_me(3,np.uint8(filter1))


# Applying Filter
c = b*filter1
fig.plot_for_me(4,np.uint8(TF.normalize(TF.log(c))))


# Inverse fourier transform(Frequency domain to space)
d = np.fft.ifft2(np.fft.fftshift(c))
fig.plot_for_me(5,np.uint8(TF.normalize(d)))
plt.show()
