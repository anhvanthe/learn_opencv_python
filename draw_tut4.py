# Feb 11, 2019
# TuongPV
# Drawing Functions in OpenCV
# Goal:
# * Learn to draw different geometric shapes with OpenCV
# * You will learn these functions :cv2.line(),cv2.circle(),cv2.rectangle(),cv2.ellipse(),cv2.putText()etc
#
# This tutorial: Drawing Polygon

import numpy as np
import cv2

# create a black image
img = np.zeros((512,512,3), np.uint8)

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,255))


cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)

cv2.imshow('image',img)

k = cv2.waitKey(0) & 0xFF

if k == 27:
    # wait for ESC key to exit
    cv2.destroyAllWindows()


else:
    # wait for 's' key to save and exit
    cv2.imwrite('Polygon.jpg',img)
    # destroys all the windows we created
    cv2.destroyAllWindows()