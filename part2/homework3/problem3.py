import cv2 as cv

img = cv.imread('data/pic2.jpg')
cv.imshow('pic2', img)

average1 = cv.blur(img, (3, 3))
cv.imshow('average blur1', average1)
average2 = cv.blur(img, (7, 7))
cv.imshow('average blur2', average2)

bilateral1 = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('bilateral blur1', bilateral1)
bilateral2 = cv.bilateralFilter(img, 10, 50, 70)
cv.imshow('bilateral blur2', bilateral2)

cv.waitKey(0)
