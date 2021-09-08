# Working with opencv-python cv2 computer vision

import cv2
import numpy as np

# second parameter decides whether the image is in color or grayscale mode
img = cv2.imread('./img1.bmp', 1)
print(img.shape)
gray = cv2.imread('./img1.bmp', 0)
print(gray.shape)
cv2.imshow('Colored Image', img)

cv2.imshow('Gray Image', gray)

#cv2 blur function
blur=cv2.blur(gray,(10,10))
cv2.imshow('Predefined Blur', blur)

#filter2D
filter1=np.ones([5,5])/25
newblur=cv2.filter2D(gray, -1, filter1)
cv2.imshow('Custom Blur', newblur)

cv2.waitKey(0)
cv2.destroyAllWindows()

