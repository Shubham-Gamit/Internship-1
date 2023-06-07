# capture a video

import cv2

framWidth = 700
frameHeight = 500
cap = cv2.VideoCapture("Resources\sample-1.mp4")

while True:
    success , img = cap.read()
    img = cv2.resize(img,(framWidth,frameHeight))
    cv2.imshow("video", img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

     