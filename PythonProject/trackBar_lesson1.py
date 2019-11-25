import cv2 as cv
import numpy as np

def nothing(x):
    pass

# create a black image, window
img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow('image')

# create trackBar
cv.createTrackbar('R', 'image', 0, 255, nothing)            #trackBary wlacza sie raz, aktualizuja sie za kazdym razem
cv.createTrackbar('G', 'image', 0, 255, nothing)            # jak cos zmienimy na nich
cv.createTrackbar('B', 'image', 0, 255, nothing)

# create switch
switch = '0 : OFF \n1 : ON'
cv.createTrackbar(switch, 'image', 0, 1, nothing)


while(1):
    cv.imshow('image', img)         # wyswietla tablice za kazdym obrotem petli
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

    #get crrent position
    r = cv.getTrackbarPos('R', 'image')
    g = cv.getTrackbarPos('G', 'image')
    b = cv.getTrackbarPos('B', 'image')
    s = cv.getTrackbarPos(switch, 'image')

    if s == 0:              # jak switch wcisniety aktualizuj tablice
        img[:] = 0
    else:
        img[:] = [b, g, r]

cv.destroyAllWindows()