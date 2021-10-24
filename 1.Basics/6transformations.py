import cv2 as cv
import numpy as np


def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


img = rescaleFrame(cv.imread('../Images/cuteCat.jpg'), .5)

cv.imshow('Cute Cat', img)


# Translation
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
#  x --> Right
#  y --> Down


translated = translate(img, -100, 100)
cv.imshow('Translated', translated)


# Rotation - OpenCV allows to shift the image according to any specified point
def rotate(img, angle, rotatePoint=None):
    (height, width) = img.shape[:2]

    if rotatePoint is None:
        rotatePoint = (width//2, height//2)

    # rotMat = cv.rotate
    rotMat = cv.getRotationMatrix2D(rotatePoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


# +Angle => AntiClockwise, -Angle => Clockwise
rotated = rotate(img, -180)
cv.imshow('Rotated', rotated)

oncemore = cv.rotate(img, rotateCode=cv.ROTATE_90_CLOCKWISE)
cv.imshow('Once More', oncemore)


# Resizing
# For shrinking the image use cv.INTER_AREA or DEFAULT
# For englarging the image use cv.INTER_LINEAR or cv.INTER_CUBIC (slower but high quality)
resized = cv.resize(img, (300, 300), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Flipping, flipCode =>
# 0 -> flips vertically, 1 -> flips horizontally, -1 -> flips both vertical and horizontally
flip = cv.flip(img, -1)
cv.imshow('Flip', flip)

# Cropping
cropped = img[200:400, 300:500]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
