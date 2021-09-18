# Binary Morphological Operations
#Erosion, Dilation

import numpy as np
import matplotlib.pyplot as plt
import cv2
from utils import Figure

fig1=Figure(1,1)

#Original Image
a=cv2.imread('./shapes.png')
fig1.plot_for_me(1,a, "Original Image")

fig2=Figure(2,2)

#filter
filt=np.ones((5,5))

#Eroded Image
b=cv2.erode(a,filt)
fig2.plot_for_me(1,b, "Eroded Image")

#Dilated Image
c=cv2.dilate(a,filt)
fig2.plot_for_me(2,c, "Dilated Image")

#Opened Image
d=cv2.morphologyEx(a, cv2.MORPH_OPEN, filt)
fig2.plot_for_me(3,d, "Opened Image")

#Closed Image
e=cv2.morphologyEx(a,cv2.MORPH_CLOSE,filt)
fig2.plot_for_me(4,e,"Closed Image")

plt.show()

