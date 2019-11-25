import cv2 as cv
import numpy as np


drawning = False    # true if mouse is pressed
mode = True         # true is draw rectangles, press 'm' to toggle to curve
ix, iy = -1, -1

def nothing(x):
    pass

def draw(event, x, y, flags, param):
    global ix, iy, drawning, r, g, b, s

    if event == cv.EVENT_LBUTTONDOWN:               #nacisniecie myszy, poczatek rysowania
        drawning = True
        ix, iy = x, y
    elif event == cv.EVENT_MOUSEMOVE:               #jezeli mysza sie rusza to narysuj figure o parametrach poczatkowych i nowych x,y
        if drawning == True:
            if s == 1:
                cv.rectangle(img, (ix, iy), (x, y), (b, g, r), -1)
            else:
                cv.circle(img, (x, y), 5, (b, g, r), -1)

    elif event == cv.EVENT_LBUTTONUP:               # jezeli puszczasz lewy guzik zakoncz zmien flage i narysuj ostatnia figure
        drawning = False
        if s == 1:
            cv.rectangle(img, (ix, iy), (x, y), (b, g, r), -1)
        else:
            cv.circle(img, (x, y), 5, (b, g, r), -1)


# create a black image, window
img = np.zeros((400, 512, 3), np.uint8)
cv.namedWindow('image')

# create trackBar, for color changes
cv.createTrackbar('R', 'image', 0, 255, nothing)
cv.createTrackbar('G', 'image', 0, 255, nothing)
cv.createTrackbar('B', 'image', 0, 255, nothing)
cv.createTrackbar('Cir/Rec', 'image', 0, 1, nothing) #change shape
cv.setMouseCallback('image', draw)                   # wait for mouse button
while(1):
    cv.imshow('image', img)         # wyswietla tablice za kazdym obrotem petli
    k = cv.waitKey(1) & 0xFF        # wait for esc
    if k == 27:
        break

    #get crrent position
    r = cv.getTrackbarPos('R', 'image')
    g = cv.getTrackbarPos('G', 'image')
    b = cv.getTrackbarPos('B', 'image')
    s = cv.getTrackbarPos('Rec/Cir', 'image')


cv.destroyAllWindows()
