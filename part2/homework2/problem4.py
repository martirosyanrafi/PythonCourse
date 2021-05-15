import cv2 as cv

img = cv.imread('data/pic2.jpg')
cv.imshow('Picture', img)

resize_area = cv.resize(img, (660, 200), interpolation=cv.INTER_AREA)
cv.imshow('Inter Area Picture', resize_area)

resize_cubic = cv.resize(img, (330, 100), interpolation=cv.INTER_CUBIC)
cv.imshow('Inter Cubic Picture', resize_cubic)

cv.waitKey(0)
