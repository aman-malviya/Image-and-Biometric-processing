#Frequency Domain Processing of Images
#Fast fourier transform (fft)

import numpy as np
import cv2
from numpy.fft import fft2
import matplotlib.pyplot as plt

a=np.float32(cv2.imread("./wb.jpg", 0))
fig=plt.figure()
fig.show()
fig.add_subplot(1,2,1)
plt.imshow(np.uint8(a), cmap="gray")
plt.axis('off')


b=np.fft.fftshift(fft2(a))
b=np.log(1+np.abs(b))
b=b-b.min()
b=255*b/b.max()
fig.add_subplot(1,2,2)
plt.imshow(np.uint8(b), cmap="gray")
plt.axis('off')
plt.show()