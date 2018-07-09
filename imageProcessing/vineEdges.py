import cv2
import numpy as np

img = cv2.imread('vine.jpg')

blur = cv2.bilateralFilter(img,4,75,75)

edges = cv2.Canny(blur, 100,170)

image, contours, hierarchy = cv2.findContours(edges,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

image = cv2.drawContours(img, contours, -1, (0,0,255), 1)

cv2.imshow('image', img)
cv2.imshow('edges', edges)
cv2.imshow('image', image)

if cv2.waitKey(0):
	cv2.destroyAllWindows()
