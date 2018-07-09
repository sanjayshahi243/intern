import cv2
import numpy as np


frame = cv2.imread('redCircle.jpg')
rframe = cv2.resize(frame, (720,480))

hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

lowerRange = np.array([0,90,20])
upperRange = np.array([10,255,255])

mask = cv2.inRange(hsv,lowerRange, upperRange)
rmask = cv2.resize(mask, (720,480))

kernel = np.ones((5,5),np.uint8)

dilation = cv2.dilate(mask,kernel,iterations = 1)
rdilation = cv2.resize(dilation, (720,480))

#erosion = cv2.erode(mask,kernel,iterations = 1)
#rerosion = cv2.resize(erosion, (720,480))

#contouring
image, contours, hierarchy = cv2.findContours(dilation,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

img = cv2.drawContours(frame, contours, -1, (255,0,0), 3)
rimg = cv2.resize(img, (720,480))

cv2.imshow('rframe', rframe)
cv2.imshow('rmask', rmask)

cv2.imshow('contour', rimg)
#cv2.imshow('erosion', rerosion)
cv2.imshow('dilation', rdilation)
#cv2.imshow('rres', rres)'''

if cv2.waitKey(0) & 0xff ==ord('q'):
	cv2.destroyAllWindows()
