import cv2 as cv

img = cv.imread('data/pic1.jpg', cv.CV_8UC1)
cv.imshow('pic1', img)


threshold, thresh = cv.threshold(img, 150, 255, cv.THRESH_BINARY)
cv.imshow('simple threshold', thresh)

adaptive_thresh = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 0)
cv.imshow('adaptive threshold', adaptive_thresh)

adaptive_thresh_gaussian = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 9)
cv.imshow('adaptive threshold gaussian', adaptive_thresh_gaussian)

cv.waitKey(0)

