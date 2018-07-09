import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('sample.jpg', 0)
rimg = cv2.resize(img, (720,480))

ret, thresh = cv2.threshold(img, 127,255,0)
rthresh = cv2.resize(thresh, (720,480))

image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#img = cv2.drawContours(img, contours, -1, (0,255,0), 5)
cnt = contours[4]
img = cv2.drawContours(img, [cnt], -1, (0,255,0), 3)
rcontour = cv2.resize(img, (720,480))

cv2.imshow('image',rimg)
cv2.imshow('contour img',rcontour)
cv2.imshow('image',rthresh)

k = cv2.waitKey(0)
if k == 27:
# wait for ESC key to exit
	cv2.destroyAllWindows()
