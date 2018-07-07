import cv2
import numpy as np
import os

cap = cv2.VideoCapture(0)

try:
	if not os.path.exists('data'):
		os.makedirs('data')
except OSError:
	print('Error in creating directory')	
	
currentFrame = 0

while(cap.isOpened()):
	ret, frame = cap.read()
	cv2.imshow('frame', frame)
	
	#splittig captured video into frames
	name = './data/frame'+str(currentFrame)+'.jpg'
	print('creating '+name)
	cv2.imwrite(name, frame)
	currentFrame += 1

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	
cap.release()
cv2.destroyAllWindows()
