import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('../../images/univers1.jpg', 0)

kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
erosion = cv.erode(img, kernel, iterations=1)
dilation = cv.dilate(img, kernel, iterations=1)
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)
blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)

cv.imshow('oryginally', img)
cv.imshow('erosion', erosion)
cv.imshow('dilation', dilation)
cv.imshow('opening', opening)
cv.imshow('closing', closing)
cv.imshow('gradient', gradient)
cv.imshow('tophat', tophat)
cv.imshow('blackhat', blackhat)

cv.waitKey(0)
cv.destroyAllWindows()