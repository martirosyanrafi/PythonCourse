import cv2 as cv

image = cv.imread('data/pic2.jpg')
cv.imshow('image', image)

image = cv.circle(image, (int(image.shape[1] / 2), int(image.shape[0] / 2)), int(image.shape[0] / 3), (0, 165, 255), 2)
cv.imshow('circle-image', image)

cv.waitKey(0)
