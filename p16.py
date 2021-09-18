#Frequency Domain Processing of Images
#Fast fourier transform (fft)

from utils import Figure,TF
import numpy as np
import cv2
import matplotlib.pyplot as plt

fig=Figure(1,2)
a=np.float32(cv2.imread("./wb.jpg", 0))
fig.plot_for_me(1,np.uint8(a))

b=np.fft.fftshift(np.fft.fft2(a))
fig.plot_for_me(2,np.uint8(TF.normalize(TF.log(b))))
plt.show()