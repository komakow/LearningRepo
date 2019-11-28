import numpy as np
import cv2 as cv


# Create a black image
img = np.zeros((512, 512, 3), np.uint8)
# Draw a diagonal blue line with thickness of 5 px : (start,stop,color,thickness)
cv.line(img, (55, 55), (111, 111), (255, 111, 111), 5)

# (top-left corner, bottom right,color, thickness)
cv.rectangle(img, (0, 0), (128, 128), (0, 255, 0), 3)

# (center, radius, color,thickness)
cv.circle(img, (156, 490), 63, (0, 0, 255), -1)

# center location, axes lengths (major axis length, minor axis length), angle is the angle of rotation of ellipse
# in anti-clockwise direction. startAngle and endAngle denotes the starting and ending of ellipse arc measured
# in clockwise direction from major axis. i.e. giving values 0 and 360 gives the full ellipse.
cv.ellipse(img, (256, 256), (80, 34), 55, 55, 260, 255, -1)

# To draw a polygon, first you need coordinates of vertices. Make those points into an array of shape ROWSx1x2
# where ROWS are number of vertices and it should be of type int32.
# Here we draw a small polygon of with four vertices in yellow color.
pts = np.array([[10, 5], [400, 30], [344, 20], [20, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv.polylines(img, [pts], True, (0, 111, 255))

#
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, 'Hello darkness', ( 10, 500), font, 2, (255, 255, 255), 2, cv.LINE_AA)

cv.imshow('frame', img)
cv.waitKey(0)
cv.destroyAllWindows()