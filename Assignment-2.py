#Image to Gray , Blur , canny , Dilated, Eroded image

import cv2
import numpy as np
img = cv2.imread("Resources\dog.png")

kernel = np.ones((5,5),np.uint8)
imGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imBlur = cv2.GaussianBlur(imGray, (7,7),0)
imgCanny = cv2.Canny(img, 100, 100)
imgDialation = cv2.dilate(imgCanny,kernel, iterations = 1)
imgEroded = cv2.erode(imgDialation, kernel, iterations = 1)

cv2.imshow("Gray Image", imGray)
cv2.imshow("Blur Image", imBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dilated Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)