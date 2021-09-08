#Sobel Filters (x-direction and y-direction)
#Gradient Magnitude

import numpy as np
import cv2

a=np.float32(cv2.imread('./wb.jpg',0))

cv2.imshow("Original Image",np.uint8(a))

#SOBEL X
filter1=np.array([[-1, 0, 1],
                  [-2, 0, 2],
                  [-1, 0, 1]])

b=cv2.filter2D(a,-1,filter1)
b=b-b.min()
b=255*b/b.max()
cv2.imshow("SOBEL (X-direction)",np.uint8(b))

#SOBEL Y
filter2=np.array([[1, 2, 1],
                  [0, 0, 0],
                  [-1,-2,-1]])

c=cv2.filter2D(a,-1,filter2)
c=c-c.min()
c=255*c/c.max()
cv2.imshow("SOBEL (Y-direction)", np.uint8(c))


#Gradient
d=(b**2+c**2)**(1/2)
d=d-d.min()
d=255*d/d.max()

cv2.imshow("Gradient Magnitude", np.uint8(d))
cv2.waitKey(0)
cv2.destroyAllWindows()


