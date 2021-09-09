# Blurring in frequency domain
# Low pass filter
# Gibbs Phenomenon (Ideal filter)

import numpy as np
import matplotlib.pyplot as plt
import cv2

#Plotting Function for minimal repition of code
class Figure:
    def __init__(self,a,b) -> None:
        self.rows=a
        self.cols=b
        self.fig=plt.figure()

    def plot_for_me(self,index,image):
        self.fig.add_subplot(self.rows,self.cols,index)
        plt.imshow(image, cmap="gray")
        plt.axis("off")
        

# Original Image
fig = Figure(2,3)
a = np.float32(cv2.imread('./build.bmp', 0))
fig.plot_for_me(1,np.uint8(a))

# Fourier Transform (space to frequency domain)
b = np.fft.fftshift(np.fft.fft2(a))
b = np.log(1+np.abs(b))
b = b-b.min()
b = 255*b/b.max()
fig.plot_for_me(2,np.uint8(b))


# Filter
r = len(a)
c = len(a[0])
filter1 = np.zeros((r, c))
radius = 50
for i in range(r):
    for j in range(c):
        if np.sqrt((i-r/2)**2+(j-c/2)**2) < radius:
            filter1[i][j] = 1
fig.plot_for_me(3,np.uint8(filter1))


# Applying Filter
c = b*filter1
c = np.log(1+abs(c))
c = c-c.min()
c = 255*c/c.max()
fig.plot_for_me(4,np.uint8(c))


# Inverse fourier transform(Frequency domain to space)
d = np.fft.ifft2(np.fft.fftshift(b*filter1))
d = np.abs(d)
d = d-d.min()
d = 255*d/d.max()
fig.plot_for_me(5,np.uint8(d))
plt.show()
