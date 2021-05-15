import cv2 as cv

img = cv.imread('data/pic2.jpg')
cv.imshow('Picture', img)

canny = cv.Canny(img, 125, 175)
cv.imshow('Edges Picture', canny)

blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
canny = cv.Canny(blur, 125, 175)
cv.imshow('Edges Blur Picture', canny)

cv.waitKey(0)
