import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# # print all available flags in Open CV
# flags = [i for i in dir(cv) if i.startswith('COLOR_')]
# print(flags)

#value of blue in HSV
blue = np.uint8([[[255, 0, 0]]])
hsv_blue = cv.cvtColor(blue, cv.COLOR_BGR2HSV)
print(hsv_blue)

# track blue and green object captured at Camera
cap = cv.VideoCapture(0)

while(1):
    _, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # range of blue
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([150, 255, 255])

    lower_green = np.array([30, 50, 50])
    upper_green = np.array([90, 255, 255])

    # treshold the hsv image to get only blue color
    mask1 = cv.inRange(hsv, lower_blue, upper_blue)
    mask2 = cv.inRange(hsv, lower_green, upper_green)

    mask = cv.add(mask1, mask2)         # add green color and blue color
 
    # bitwise-AND mask and original image
    res = cv.bitwise_and(frame, frame, mask=mask)

    #show
    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
cap.release()