#Principal Component Ananlysis
# Picking points from an Image and showing them on the Plot

import numpy as np
import matplotlib.pyplot as plt
from utils import Figure
import cv2

fig=Figure(1,2)

a=cv2.imread('./point.png',0)
fig.plot_for_me(1, np.uint8(a), "Image")

row,col=np.where(a==255)
fig.plot_for_me(2,[[]],"Plot")
plt.scatter(col,row, marker=".", color="red")
plt.xlim(0,1400)
plt.ylim(0,700)

plt.show()
