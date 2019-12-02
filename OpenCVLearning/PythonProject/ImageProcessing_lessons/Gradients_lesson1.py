import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('../../images/krata2.jpg', 0)
img = cv.bilateralFilter(img, 17, 80, 80)       # rozmycie
img = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 5, 2)     # binaryzacja

sobelx = cv.Sobel(img, cv.CV_8U, 1, 0, ksize=5)         # used uint8
sobely = cv.Sobel(img, cv.CV_8U, 0, 1, ksize=5)
laplacian = cv.Laplacian(img, cv.CV_64F)                # used 64F

ad = cv.add(sobelx,sobely)

cv.imshow('img', img)
cv.imshow('laplacian', laplacian)
cv.imshow('sobelx', sobelx)
cv.imshow('sobely', sobely)
cv.imshow('ad', ad)

cv.waitKey(0)
cv.destroyAllWindows()