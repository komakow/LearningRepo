import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


img = cv.imread('../../images/free-photo-twin-fowers-407-m.jpg', 1)
height, width = img.shape[:2]
res = cv.resize(img, (2*width, 2*height), interpolation=cv.INTER_CUBIC)


# cv.imshow('res', res)
# cv.imshow('img', img)
# cv.waitKey(0)
# cv.destroyAllWindows()

print('*********************************')
# translation
img = cv.imread('../../images/free-photo-twin-fowers-407-m.jpg', 0)
rows, cols = img.shape

M = np.float32([[1, 0, 100], [0, 1, 50]])
dst = cv.warpAffine(img, M, (cols, rows))

# cv.imshow('dst', dst)
# cv.imshow('img', img)
# cv.waitKey(0)
# cv.destroyAllWindows()

print('*********************************')
# Rotation
img = cv.imread('../../images/free-photo-twin-fowers-407-m.jpg', 0)
rows, cols = img.shape
M = cv.getRotationMatrix2D(((cols-1)/2.0, (rows-1)/2.0), 22, 1)
dst = cv.warpAffine(img, M, (cols, rows))

# cv.imshow('dst', dst)
# cv.imshow('img', img)
# cv.waitKey(0)
# cv.destroyAllWindows()

print('*********************************')
# Affine Transformation
img = cv.imread('../../images/free-photo-twin-fowers-407-m.jpg', 0)
rows, cols = img.shape

pts1 = np.float32([[50, 50], [200, 50], [50, 200]])     # coordinates of point which should be shifted
pts2 = np.float32([[0, 0], [200, 200], [100, 250]])     # coordinates of shifted points

M = cv.getAffineTransform(pts1, pts2)
dst = cv.warpAffine(img, M, (cols, rows))

cv.imshow('dst', dst)
cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()