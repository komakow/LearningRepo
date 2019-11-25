import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('../../images/ludzie1.jpg', 1)
px = img[100, 100]
print(px)
green = img[100,100,1]  #b,g,r
print(green)

img[100, 100] = [255, 255, 255]  # access and modify specific pixel
print(img[100,100])

img = cv.imread('../../images/abcd.jpg', 1)  # re read image
# better pixel accessing
print(img.item(100, 100, 1))

print(img.shape)   # print number of rows, columns and color channels (if photo is grey touple will not returned channel)

print(img.size)     # number of pixels

print(img.dtype)    # data type of photo
print("*********************************")

# plt.imshow(img)     # show photo
# plt.show()
# select some part of photo and copy it to other part of photo

foo = img[120:220, 220:320]
img[300:400, 200:300] = foo
# plt.imshow(img)     # show photo
# plt.show()

b,g,r = cv.split(img)
img = cv.merge((r,g,b))     #change to RGB color
# plt.imshow(img)     # show photo
# plt.show()

img[:,:,2] = 0  #set all the blue pixels to zerooo
# plt.imshow(img)     # show photo
# plt.show()

img = cv.imread('../../images/abcd.jpg', 1)  # re read image

print("*********************************")

BLUE = [255, 0, 0]

# borders for image. Nice method for shows images

replicate = cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img,50,50,50,50,cv.BORDER_WRAP)
constant = cv.copyMakeBorder(img,50,10,10,10,cv.BORDER_CONSTANT, value=BLUE)

# plt.subplot(231),plt.imshow(img,'gray'),plt.title('ORIGINAL')
# plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
# plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
# plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
# plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
#plt.subplot(236),\
plt.imshow(wrap,'gray'),plt.title('CONSTANT')

plt.show()