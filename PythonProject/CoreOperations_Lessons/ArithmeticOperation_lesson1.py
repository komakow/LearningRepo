import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img1 = cv.imread('../../images/free-photo-Statue-38-m.jpg', 1)          # the same size as photo below
img2 = cv.imread('../../images/free-photo-twin-fowers-407-m.jpg', 1)

dst = cv.addWeighted(img1, 0.7, img2, 0.5, 0)           # marge two photo with any weight

# cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows()


#***************************************Add two photo with foreground and background************************
print('******************')
img1 = cv.imread('../../images/free-photo-Statue-38-m.jpg', 1)  # small
img2 = cv.imread('../../images/ludzie_krajobraz.jpg', 1)        # big


rows, cols, channels = img1.shape   # get photo params
roi = img2[0:rows, 0:cols]          # make Region Of Interest (ROI) at secont pic

# Now create a mask of logo and create its inverse mask also
img1gray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(img1gray, 120, 255, cv. THRESH_BINARY)     # make color photo to binary photo
mask_inv = cv.bitwise_not(mask)


# black out the area of small pic in ROI
img2_bg = cv.bitwise_and(roi, roi, mask=mask_inv)       # place at big photo binary mask from small photo


# take only region of logo from image
img1_fg = cv.bitwise_and(img1, img1, mask=mask)         # place at small photo binary mask from small photo


# put logo in ROI and modify the main image
# add background and foreground. Black color has value of '0', so add black and blue = blue :)
dst = cv.add(img2_bg, img1_fg)

cv.imshow('img2_bg', img2_bg)
cv.imshow('img1_fg', img1_fg)
cv.imshow('dst', dst)
cv.waitKey(0)

img2[0:rows, 0:cols] = dst

cv.imshow('res', img2)
cv.waitKey(0)
cv.destroyAllWindows()


