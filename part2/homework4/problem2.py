import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('data/pic1.jpg')
cv.imshow('img', img)

colors = ('b', 'g', 'r')

for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0, 256])
    x = np.arange(256)
    plt.plot(x, hist, color=col)
    plt.title('Color Histogram')
    plt.xlabel('Bins')
    plt.ylabel('# of pixels')

plt.show()
