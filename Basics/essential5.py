import cv2 as cv


def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


img = rescaleFrame(cv.imread('Basics/Images/cuteCat.jpg'), .5)
cv.imshow("Cuteee Cat", img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Blur to increase the blur  ↓ increase these values
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

# Edge Cascade
canny = cv.Canny(img, 125, 175)
cv.imshow("Canny Edges", canny)

# Dilating the image
dilated = cv.dilate(canny, (9, 9), iterations=3)
cv.imshow("Dilated", dilated)

# Eroding
erode = cv.erode(dilated, (3, 3), iterations=1)
cv.imshow("Eroded", erode)

cv.waitKey(0)
