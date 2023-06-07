#merge images


import cv2
import numpy as np

img = cv2.imread("Resources\dog.png")
imghor = np.hstack((img,img))
imgver = np.vstack((img,img))

imghor1 = np.hstack((img,img,img))
imgver1 = np.vstack((img,img,img))

imgResize = cv2.resize(imghor,(800,500))

cv2.imshow("Image", img)
cv2.imshow("Horizontal", imghor)
cv2.imshow("Vertical", imgver)
cv2.imshow("Horizontal", imghor1)
cv2.imshow("Vertical", imgver1)

cv2.waitKey(0)
