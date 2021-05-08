import cv2 as cv


def rescale_frame(frame, scale):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


image = cv.imread('data/pic1.jpg')
image_rescaled = rescale_frame(image, 0.5)

cv.imshow('image', image)
cv.imshow('image_rescaled', image_rescaled)

cv.waitKey(0)
