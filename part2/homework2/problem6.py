import cv2 as cv

img = cv.imread('data/pic3.jpg')
cv.imshow('Picture', img)

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Picture', canny)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('Gray Blur Picture', blur)

cv.waitKey(0)