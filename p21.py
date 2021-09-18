#Detecting Ridge Endings and Bifurcations

import numpy as np
import matplotlib.pyplot as plt
import cv2
from utils import Figure
from skimage.morphology import thin

fig=Figure(2,2)

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

#Crossing Number Calculation
row=len(a)
col=len(a[0])
CN=np.zeros((row,col))

for i in range(2,row-1):
    for j in range(2,col-1):
        if(c[i,j] == 1):
            arr1=np.array([c[i-1,j-1], c[i-1,j], c[i-1,j+1], c[i,j+1],c[i+1,j+1],c[i+1,j],c[i+1,j-1],c[i,j-1]])
            arr2=arr1[1::]
            arr2=np.append(arr2,arr1[0])
            CN[i,j]=(1/2)*(sum(abs(arr1-arr2)))

ridge_row, ridge_col=np.where(CN == 1)
bf_row, bf_col=np.where(CN == 3)

fig.plot_for_me(4,np.uint8(c*255), "Bifurcations and Ridge endings")
plt.scatter(ridge_col, ridge_row, marker=".", color="r")
plt.scatter(bf_col, bf_row, marker=".", color="yellow")
plt.legend(['Ridge Endings', 'Bifurcations'], loc="lower right")

fig2=Figure(1,1)
fig2.plot_for_me(1,np.uint8(a), "Bifurcations and Ridge Endings on Actual Fingerprint")
plt.scatter(ridge_col, ridge_row, marker=".", color="r")
plt.scatter(bf_col, bf_row, marker=".", color="yellow")
plt.legend(['Ridge Endings', 'Bifurcations'], loc="lower right")

plt.show()