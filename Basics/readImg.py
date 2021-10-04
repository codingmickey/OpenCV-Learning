import cv2 as cv

# Reads the image
img = cv.imread('Basics/Images/cuteCat.jpg')

# Shows the images with (windowName, img)
cv.imshow("Cute Cat", img)

# Waits for any key to be pressed
cv.waitKey(0)
