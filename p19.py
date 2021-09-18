#Generating Mask, Extracting ROI

import numpy as np
import matplotlib.pyplot as plt
import cv2
from utils import Figure

fig=Figure(1,3)

#Original Image
a=np.float32(cv2.imread('./fp.jpg',0))
fig.plot_for_me(1,np.uint8(a),"Original Image")

#Low Pass Filter
n=35
filt=np.ones((n,n))/n**2

#Filtered Image
b=cv2.filter2D(a,-1,filt)
fig.plot_for_me(2,np.uint8(b),"Blurred Image")

#Thresholding
c=(b<200)
c=c*255
fig.plot_for_me(3,np.uint8(c),"Mask")


plt.show()