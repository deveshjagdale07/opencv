import cv2
import numpy as np
img=cv2.imread("orange.jpg")
dst=cv2.fastNlMeansDenoisingColored(img,None,10,10,7,4)
cv2.imshow("original_img",img)
cv2.imshow("denoising_img",dst)
