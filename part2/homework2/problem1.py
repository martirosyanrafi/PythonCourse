import cv2 as cv

img = cv.imread('data/pic1.jpg')

cv.imshow('Picture', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Picture', gray)

cv.waitKey(0)