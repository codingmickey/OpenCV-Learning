import cv2 as cv

# Reads the image
img = cv.imread('../Images/cuteCat.jpg')

# Shows the images with (windowName, img)
cv.imshow("Cute Cat", img)

# Waits for any key to be pressed
cv.waitKey(0)

# Note: When large images are output then the image goes
# offscreen as OpenCV doesn't have any inbuilt processing
