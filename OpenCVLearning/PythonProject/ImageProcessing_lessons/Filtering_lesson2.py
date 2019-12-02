import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

cap = cv.VideoCapture(0)

# filtering
while(1):
    _, img = cap.read()

    # blur = cv.blur(img, (2, 2)) # zwykly blur
    # blur = cv.GaussianBlur(img, (9, 9), 0)  #gausian blur
    # blur = cv.medianBlur(img, 5)  # median blurring
    blur = cv.bilateralFilter(img, 17, 170, 170)   # great in noise removal while keeping edges sharp

    cv.imshow('blur', blur)

    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
cap.release()