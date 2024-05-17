import cv2
import numpy as np
img=cv2.imread("tiger.jpg")
kernel=np.ones((3,3),dtype="uint8")
img_dilation=cv2.dilate(img,kernel,iterations=1)
img_erosion=cv2.erode(img,kernel,iterations=1)
cv2.imshow("input",img)
cv2.imshow("erosion",img_erosion)
cv2.imshow("dilation",img_dilation)
cv2.waitKey(0)
