import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

#load a color image in greyscale

img = cv.imread('../images/ludzie1.jpg', 1)
b,g,r = cv.split(img)
img2 = cv.merge([r, g, b])
plt.subplot(121);plt.imshow(img) # expects distorted color
plt.subplot(222);plt.imshow(img2) # expect true color
plt.show()