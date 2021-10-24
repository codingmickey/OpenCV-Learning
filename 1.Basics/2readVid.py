import cv2 as cv

# Reading Videos
# this function takes in a parameter
# -> Path of the video
# -> 0, 1, 2 - the video source of webcam or USB cam
capture = cv.VideoCapture('../Videos/catVideo.mp4')

# Loop through each frame to display it
while True:
    isTrue, frame = capture.read()

    cv.imshow("Video", frame)

    # Break if the video is over or the 'd' key is pressed
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
