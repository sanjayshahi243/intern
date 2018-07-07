#resized_image = cv2.resize(image, (100, 50)) 

import numpy as np
import cv2

image = cv2.imread('sample.jpg',1)
resized_image = cv2.resize(image, (720, 480)) 

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lowerGreen = np.array([40,30,20])
upperGreen = np.array([60,255,255])

mask = cv2.inRange(hsv,lowerGreen, upperGreen)
resized_mask = cv2.resize(mask, (720, 480)) 

res = cv2.bitwise_and(image,image,mask=mask)
resized_res = cv2.resize(res, (720, 480)) 

cv2.imshow('image',resized_image)
cv2.imshow('mask',resized_mask)
cv2.imshow('res',resized_res)


k = cv2.waitKey(0)
if k == 27:
# wait for ESC key to exit
	cv2.destroyAllWindows()
