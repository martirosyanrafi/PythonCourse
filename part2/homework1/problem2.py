import cv2 as cv

capture = cv.VideoCapture('data/vid1.mp4')

while True:
    isTrue, frame = capture.read()

    if isTrue:
        cv.imshow('Video', frame)
    else:
        exit(1)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)
