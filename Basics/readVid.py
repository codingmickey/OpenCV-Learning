import cv2 as cv

# Reading Videos
capture = cv.VideoCapture('Basics/Videos/catVideo.mp4')

# Loop through each frame to display it
while True:
    isTrue, frame = capture.read()

    cv.imshow("Video", frame)

    # Break if the video is over or the 'd' key is pressed
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
