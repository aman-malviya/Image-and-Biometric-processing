# Blurring in frequency domain
# Low pass filter
# Gibbs Phenomenon (Ideal filter)

import numpy as np
import matplotlib.pyplot as plt
import cv2

# Original Image
fig = plt.figure()
fig.show()
a = np.float32(cv2.imread('./build.bmp', 0))
fig.add_subplot(2, 3, 1)
plt.imshow(np.uint8(a), cmap="gray")
plt.axis('off')

# Fourier Transform (space to frequency domain)
b = np.fft.fftshift(np.fft.fft2(a))
b = np.log(1+np.abs(b))
b = b-b.min()
b = 255*b/b.max()
fig.add_subplot(2, 3, 2)
plt.imshow(np.uint8(b), cmap="gray")
plt.axis('off')

# Filter
r = len(a)
c = len(a[0])
filter1 = np.zeros((r, c))

radius = 50

for i in range(r):
    for j in range(c):
        if np.sqrt((i-r/2)**2+(j-c/2)**2) < radius:
            filter1[i][j] = 1

fig.add_subplot(2, 3, 3)
plt.imshow(np.uint8(filter1), cmap="gray")
plt.axis('off')

# Applying Filter
c = b*filter1
c = np.log(1+abs(c))
c = c-c.min()
c = 255*c/c.max()
fig.add_subplot(2, 3, 4)
plt.imshow(np.uint8(c), cmap="gray")
plt.axis('off')

# Inverse fourier transform(Frequency domain to space)
d = np.fft.ifft2(np.fft.fftshift(b*filter1))
d = np.abs(d)
d = d-d.min()
d = 255*d/d.max()
fig.add_subplot(2, 3, 5)
plt.imshow(np.uint8(d), cmap="gray")
plt.axis('off')
plt.show()
