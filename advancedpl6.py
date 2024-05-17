import cv2
from matplotlib import pyplot as plt
img=cv2.imread("orange.jpg")
hist=cv2.calcHist([img],[0],None,[256],[0,256])
cv2.imshow("original_img",img)
plt.plot(hist)
plt.show()
