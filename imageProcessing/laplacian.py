import cv2
import numpy as np

img = cv2.imread('vine.jpg')

laplacian = cv2.Laplacian(img, cv2.CV_64F)

cv2.imshow('image', img)
cv2.imshow('laplacian', laplacian)

if cv2.waitKey(0):
	cv2.destroyAllWindows()

