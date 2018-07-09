import cv2
import numpy as np


frame = cv2.imread('sample.jpg')
rframe = cv2.resize(frame, (720,480))

hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

lowerGreen = np.array([40,30,20])
upperGreen = np.array([60,255,255])

mask = cv2.inRange(hsv,lowerGreen, upperGreen)
rmask = cv2.resize(mask, (720,480))

res = cv2.bitwise_and(frame,frame,mask=mask)
rres = cv2.resize(res, (720,480))

cv2.imshow('rframe', rframe)
cv2.imshow('rmask', rmask)
cv2.imshow('rres', rres)

if cv2.waitKey(0) & 0xff ==ord('q'):
	cv2.destroyAllWindows()
