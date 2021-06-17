import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('data/pic1.jpg')
cv.imshow('img', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256])
gray_hist = [i[0] for i in gray_hist]

x = np.arange(256)
plt.plot(x, gray_hist)
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')

plt.show()
