import numpy as np
import cv2 as cv


cap = cv.VideoCapture(0)
#define the codec and create videoWriter object
fourcc  = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('../save/output1.avi',fourcc, 20.0, (640, 480))
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    #capture frame by frame
    ret, frame = cap.read()

    if not ret:
        print("Cant receive frame.... ")
        break

    frame = cv.flip(frame, -1)
    out.write(frame)
    cv.imshow('frame',frame)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
out.release()
cv.destroyAllWindows()