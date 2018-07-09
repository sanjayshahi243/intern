import cv2
import numpy as np


frame = cv2.imread('sample.jpg')
rframe = cv2.resize(frame, (720,480))

hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

lowerGreen = np.array([40,90,20])
upperGreen = np.array([80,255,255])

mask = cv2.inRange(hsv,lowerGreen, upperGreen)
rmask = cv2.resize(mask, (720,480))

#eroding and dilating the masked image
kernel = np.ones((5,5),np.uint8)
#opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
#ropening = cv2.resize(opening, (720,480))

'''erosion = cv2.erode(mask,kernel,iterations = 5)
rerosion = cv2.resize(erosion, (720,480))'''
dilation = cv2.dilate(mask,kernel,iterations = 25)
rdilation = cv2.resize(dilation, (720,480))
erosion = cv2.erode(dilation,kernel,iterations = 25)
rerosion = cv2.resize(erosion, (720,480))

#contouring
image, contours, hierarchy = cv2.findContours(erosion,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

img = cv2.drawContours(frame, contours, -1, (255,0,0), 7)
rimg = cv2.resize(img, (720,480))

cv2.imshow('rframe', rframe)
cv2.imshow('rmask', rmask)
#cv2.imshow('opening', ropening)
cv2.imshow('contour', rimg)
cv2.imshow('erosion', rerosion)
cv2.imshow('dilation', rdilation)
#cv2.imshow('rres', rres)'''

if cv2.waitKey(0) & 0xff ==ord('q'):
	cv2.destroyAllWindows()
