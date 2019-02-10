# Feb 10, 2019
# TuongPV
# To lear using opencv with numpy and matplotlib

# import numpy as np
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('mainboard.jpg',0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
plt.show()