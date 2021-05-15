import cv2 as cv

img = cv.imread('data/pic1.jpg')

cv.imshow('Picture', img)

blur1 = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
cv.imshow('Blue Picture 1', blur1)

blur2 = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('Blur Picture 2', blur2)

cv.waitKey(0)
