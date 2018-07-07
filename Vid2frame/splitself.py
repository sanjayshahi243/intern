import cv2
import numpy as np
import os

cap = cv2.VideoCapture('flame.avi')

try:
	if not os.path.exists('data'):
		os.makedirs('data')
except OSError:
	print('Error: Creating of directory ')

currentFrame = 0 

while(cap.isOpened()):
	ret, frame = cap.read()
	#print(ret, frame)
	#print(cap)
	
	name = './data/selfframe'+str(currentFrame)+'.jpg'
	print('Creating '+name)
	
	#cv2.imshow('frame', frame)	

	cv2.imwrite(name, frame)
	currentFrame += 1
	#if currentFrame > 20:
	#	break

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	
	
