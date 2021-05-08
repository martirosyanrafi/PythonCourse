import cv2 as cv


def rescale_frame(frame, scale):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


capture = cv.VideoCapture('data/vid1.mp4')

while True:
    isTrue, frame = capture.read()

    if frame is not None:
        frame_rescaled = rescale_frame(frame, 0.5)
        cv.imshow('video', frame)
        cv.imshow('video_rescaled', frame_rescaled)
    else:
        exit(1)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)
