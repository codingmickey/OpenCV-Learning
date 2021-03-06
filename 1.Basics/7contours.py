import cv2 as cv
import numpy as np


def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


img = rescaleFrame(cv.imread('../Images/thumbs_up_down.jpg'))
cv.imshow('Raw', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# METHOD 1

blur = cv.GaussianBlur(gray, (3, 3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny edges', canny)

# METHOD 2

# this will convert the image into a binary image like
# if intensity below 125 then it sets to 0(Black), else sets to 255(White)
ret, thresh = cv.threshold(gray, 225, 255, cv.THRESH_BINARY_INV)
cv.imshow('Thresh', thresh)

# modes
# cv.RETR_TREE --> all the hierarchical contours
# cv.RETR_EXTERNAL --> all the external contours
# cv.RETR_LIST --> all the contours in the image

# method --> Eg. for a line in the image
# cv.CHAIN_APPROX_NONE --> gets all the co-ordintes of the points on the line
# cv.CHAIN_APPROX_SIMPLE --> compresses into such that make more sense eg. shows 2 points
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found')

cv.drawContours(img, contours, -1, (0, 255, 0), 2)
cv.imshow('Contours drawn', img)

cv.imwrite('Contours.jpg', img)

cv.waitKey(0)
