# Feb 10, 2019
# TuongPV
# Getting Started with Videos
# Goal:
# * Learn to read video, display video and save video.
# * Learn to capture from Camera and display it.
# * You will learn these functions : cv2.VideoCapture(), cv2.VideoWriter()
#
# This tutorial learn Capture Video from Camera

import numpy as np
import cv2
import time
import sys, os, random, hashlib
from math import *

cap = cv2.VideoCapture(0)

while(True):
	# capture frame by frame
	ret, frame = cap.read()

	# Our operations on the frame come here
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


	# Display the resulting frame
	cv2.imshow('frame', gray)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break


# When everything done, release the capture
cap.release()

cv2.destroyAllWindows()
