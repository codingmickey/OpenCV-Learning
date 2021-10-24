import cv2 as cv
import numpy as np


img = cv.imread('Basics/Images/thumbs_up_down.jpg')
# cv.imshow('Cute Cat', img)

blur = cv.GaussianBlur(img, (0, 0), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)


ret, thresh = cv.threshold(gray, 225, 255, cv.THRESH_BINARY_INV)
# cv.imshow('Thresh', thresh)

tresh1 = cv.cvtColor(thresh, cv.COLOR_GRAY2BGR)
both = np.hstack((blur, tresh1))

cv.imshow('Both', both)


cv.waitKey(0)
