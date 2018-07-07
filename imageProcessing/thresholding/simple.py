import cv2
import numpy as np
#from matplotlib import pyplot as plt

img = cv2.imread('sample.jpg', 0 )
rimg = cv2.resize(img , (720,480))

ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
rthresh1 = cv2.resize(thresh1 , (720,480))

ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
rthresh2 = cv2.resize(thresh2 , (720,480))

cv2.imshow('image',rimg)
cv2.imshow('thresh1',rthresh1)
cv2.imshow('thresh2',rthresh2)
if cv2.waitKey(0):
	cv2.destroyAllWindows()
