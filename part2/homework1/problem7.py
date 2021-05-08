import cv2 as cv

image = cv.imread('data/pic1.jpg')
cv.imshow('image', image)

image = cv.line(image, (image.shape[1], 0), (0, image.shape[0]), (0, 0, 255), 3)
cv.imshow('line-image', image)

cv.waitKey(0)
