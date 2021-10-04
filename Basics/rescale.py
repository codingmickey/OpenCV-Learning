import cv2 as cv


def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def changeRes(width, height):
    # Live Video
    capture.set(3, width)
    capture.set(4, height)


# ------ Reading Live Video ------
live_video = cv.VideoCapture(0)

# Loop through each frame to display it
while True:
    isTrue, frame = live_video.read()

    cv.imshow("Live Video", frame)

    # Break if the video is over or the 'd' key is pressed
    if cv.waitKey(20) & 0xFF == ord('s'):
        break

live_video.release()


# ------ Reading Images ------
img = cv.imread('Basics\Images\cuteCat.jpg')

# Shows the images with (windowName, img)
cv.imshow("Cute Cat", img)

resized_image = rescaleFrame(img, 0.5)

cv.imshow("Resized Kawaai cat", resized_image)

# Waits for any key to be pressed
cv.waitKey(0)


# ------ Reading Videos ------
capture = cv.VideoCapture('Basics/Videos/catVideo.mp4')

# Loop through each frame to display it
while True:
    isTrue, frame = capture.read()

    frame_resize = rescaleFrame(frame, .3)

    cv.imshow("Video", frame)
    cv.imshow("Rescaled Video", frame_resize)

    # Break if the video is over or the 'd' key is pressed
    if cv.waitKey(20) & 0xFF == ord('s'):
        break

capture.release()
cv.destroyAllWindows()
