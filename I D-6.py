#Image Crop and Resize
import cv2
import numpy as np
img = cv2.imread("Resources\dog.png")

print(img.shape)

imgResize = cv2.resize(img,(100,500))
imgCropped = img[0:100,100:500]
cv2.imshow("Original image", img)
cv2.imshow("Original image", imgResize)
cv2.imshow("Original image", imgCropped)

cv2.waitKey(0)









