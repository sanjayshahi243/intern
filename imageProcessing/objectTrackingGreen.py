import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
	_, frame = cap.read()
	
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	lowerGreen = np.array([40,30,20])
	upperGreen = np.array([60,255,255])

	mask = cv2.inRange(hsv,lowerGreen, upperGreen)
	
	res = cv2.bitwise_and(frame,frame,mask=mask)

	cv2.imshow('frame', frame)
	cv2.imshow('mask', mask)
	cv2.imshow('res', res)

	if cv2.waitKey(1) & 0xff ==ord('q'):
		break
cv2.destroyAllWindows()
