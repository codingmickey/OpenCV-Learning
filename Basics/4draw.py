import cv2 as cv
import numpy as np

# Make a blank canvas of 500x500
blank = np.zeros((500, 500, 3), dtype="uint8")
cv.imshow("Blank", blank)

# 1. Paint the image a certain color
blank[200:300, 300:400] = 0, 0, 255  # BGR
cv.imshow("Red Square", blank)

# 2. Draw a Rectangle

# An outlined Rectangle
# cv.rectangle(blank, (0, 0), (250, 250),  (0, 255, 0), thickness=2)

# An filled Square with half the size of canvas
cv.rectangle(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2),  (0, 255, 0), thickness=-1)
cv.imshow("New Rectangle", blank)

# Filled Rectangle with
# thickness=cv.FILLED
# thickness=-1
cv.rectangle(blank, (0, 0), (250, 500),  (0, 255, 0), thickness=cv.FILLED)
cv.imshow("Rectangle", blank)

# 3. Draw a Circle

cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 54, (255, 0, 0), thickness=-1)
cv.imshow("Circle", blank)

# 4. Draw a line

cv.line(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), thickness=3)
cv.imshow("Line", blank)

# 5. Write Text
cv.putText(blank, "Hello Kartik!", (0, 255), cv.FONT_HERSHEY_TRIPLEX, 1.5, (102, 203, 255), thickness=2)
cv.imshow("Text", blank)

cv.waitKey(0)
