#Detecting Vertical Bifurcations, Naive approach
#Doubt

import numpy as np
import matplotlib.pyplot as plt
import cv2
from utils import Figure, TF
from skimage.morphology import thin

fig=Figure(1,4)

#Original Image
a=np.float32(cv2.imread('./fp2.png',0))
fig.plot_for_me(1,np.uint8(a),"Original Image")

#Binarized Image
b=(a<128)
fig.plot_for_me(2,np.uint8(b*255),"Binarized Image")

#Thinned Image
c=thin(b)
c=1*c
fig.plot_for_me(3,np.uint8(c*255),"Thinned Image")

#Bifurcation Filter
filt=np.array([
    [1,0,1],
    [0,1,0],
    [0,1,0]
])
d=cv2.filter2D(np.float32(c*255), -1, filt)
mx=d.max()
row,col=np.where(d==mx)
fig.plot_for_me(4,np.uint8(c*255),"Vertical Bifurcations")
plt.scatter(col,row,marker=".", color="b")

plt.show()