# Learning Point detector
import numpy as np
import cv2
import matplotlib.pyplot as plt

a=np.float32(cv2.imread('./wb.jpg', 0))

cv2.imshow("Original Image", np.uint8(a))


# Filters
filter1=np.array([
                  [-1,-1,-1],
                  [-1,8,-1],
                  [-1,-1,-1]
                ])

b=cv2.filter2D(a,-1,filter1)
b=b-b.min()
b=255*(b/b.max())
cv2.imshow("Filtered Image", np.uint8(b))

cv2.waitKey(0)
cv2.destroyAllWindows()