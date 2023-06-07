#insert shape in an image

import cv2
import numpy as np

img = cv2.imread("Resources\dog.png")

print(img.shape)
cv2.rectangle(img,(0,0),(240,350),(0,0,255),3)
cv2.circle(img,(240,350),5,(0,255,0),3)
cv2.imshow("Image",img)
cv2.waitKey(0)