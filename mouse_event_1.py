# Feb 11, 2019
# TuongPV
# Mouse as a Paint-Brush
# Goal:
# * Learn to handle mouse events in OpenCV
# * You will learn these functions :cv2.setMouseCallback()
#
# This tutorial: Mouse event

import numpy as np
import cv2

event = [i for i in dir(cv2) if 'EVENT' in i]

print event