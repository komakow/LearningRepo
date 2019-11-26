import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

e1 = cv.getTickCount()
#user code below
img = cv.imread('../../images/abcd.jpg', 1)  # re read image
e2 = cv.getTickCount()

time = (e2-e1) /cv.getTickFrequency()

print(time)
print(cv.getTickFrequency())        # frequent of program 'tick'

print(cv.useOptimized())            # check if CV used optimization
# module IPython have a lot of good measuring options!!!!!
