#Face Detection

import cv2
faceCascade = cv2.CascadeClassifier("haar-cascade-files-master\haar-cascade-files-master\haarcascade_frontalface_alt.xml")
img = cv2.imread("Resources\Group.jpeg.jpg")
imGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imGray, 1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w , y+h),(0,255,0),3)

    cv2.imshow("result",img)
    cv2.waitKey(0)