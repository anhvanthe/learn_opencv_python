# Feb 10, 2019
# TuongPV
# Getting Started with Videos
# Goal:
# * Learn to read video, display video and save video.
# * Learn to capture from Camera and display it.
# * You will learn these functions : cv2.VideoCapture(), cv2.VideoWriter()
#
# This tutorial learn Capture Video from A file

import numpy as np
import cv2

cap = cv2.VideoCapture('ADS.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

# End of file