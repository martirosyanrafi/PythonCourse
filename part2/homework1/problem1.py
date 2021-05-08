import cv2 as cv

image_paths = ['data/pic1.jpg', 'data/pic2.jpg', 'data/pic3.jpg']

for path in image_paths:
    image = cv.imread(path)
    cv.imshow(path, image)

cv.waitKey(0)
