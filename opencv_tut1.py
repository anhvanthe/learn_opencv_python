# Feb 10, 2019
# TuongPV
# To lear using opencv and basic function: open and save image

# import numpy as np
import cv2

# Load an color image in grayscale
# Use the cv2.imread()to read an image
# cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected.  It is the defaultflag.
# cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
# cv2.IMREAD_UNCHANGED : Loads image as such including alpha channe
img = cv2.imread('mainboard.jpg',0)
# just for test
# print img

# you can resize window
cv2.namedWindow('image', cv2.WINDOW_NORMAL)

# Now, show the image, using cv2.imshow()
# image will be showed as GRAYED image
cv2.imshow('image',img)

# cv2.waitKey()is  a  keyboard  binding  function.   Its  argument  is  the  time  in  milliseconds
# k = cv2.waitKey(0)
# for x64 machine
k = cv2.waitKey(0) & 0xFF

if k == 27:
	# wait for ESC key to exit
	cv2.destroyAllWindows()
	

else:
	# wait for 's' key to save and exit
	cv2.imwrite('mainboard_gray.jpg',img)
	# destroys all the windows we created
	cv2.destroyAllWindows()
