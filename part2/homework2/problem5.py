import cv2 as cv
import numpy as np

img = cv.imread('data/pic1.jpg')
cv.imshow('Picture', img)


def translate(img, x, y):
    trans_mat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])

    return cv.warpAffine(img, trans_mat, dimensions)


translated = translate(img, 50, 200)
cv.imshow('Translated Picture', translated)


def rotate(img, angle, rot_point=None):

    (height, width) = (img.shape[0], img.shape[1])

    if rot_point is None:
        rot_point = (width // 2, height // 2)

    rot_mat = cv.getRotationMatrix2D(rot_point, -angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rot_mat, dimensions)


rotated = rotate(translated, 50)
cv.imshow('Rotated Picture', rotated)

flip = cv.flip(rotated, -1)
cv.imshow('Flipped Picture', flip)

cv.waitKey(0)
