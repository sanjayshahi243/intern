import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
	_, frame = cap.read()
	
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	lowerRed = np.array([0,30,20])
	upperRed = np.array([10,255,255])

	mask = cv2.inRange(hsv,lowerRed, upperRed)
	
	res = cv2.bitwise_and(frame,frame,mask=mask)

	cv2.imshow('frame', frame)
	cv2.imshow('mask', mask)
	cv2.imshow('res', res)

	if cv2.waitKey(1) & 0xff ==ord('q'):
		break
cv2.destroyAllWindows()
