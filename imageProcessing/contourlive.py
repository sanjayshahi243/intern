import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
	ret, frame = cap.read()

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	lowerRed = np.array([0,30,20])
	upperRed = np.array([5,255,255])

	mask = cv2.inRange(hsv,lowerRed, upperRed)
	
	kernel = np.ones((5,5),np.uint8)
	erosion = cv2.erode(mask,kernel,iterations = 1)

	dilation = cv2.dilate(erosion,kernel,iterations = 5)

	#contouring live image
	image, contours, hierarchy = cv2.findContours(dilation,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	img = cv2.drawContours(frame, contours, -1, (255,0,0), 3)
	rimg = cv2.resize(img, (720,480))
		
	cv2.imshow('frame', frame)
	cv2.imshow('mask', mask)
	cv2.imshow('erosion', erosion)
	#cv2.imshow('dilation', dilation)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	
cap.release()
cv2.destroyAllWindows()
