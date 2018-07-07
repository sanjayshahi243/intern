import cv2
import numpy as np
import os

cap = cv2.VideoCapture(0) # 0 implies first camera on computer, in laptop webcam
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('outputGray.avi', fourcc, 20.0, (640,480))	#creating VideoWriter Object and passing 'name', codec, framerate, videosize

'''try:
	if not os.path.exists('output'):
		os.makedirs('output')
except OSError:
	print('Error creating directory')
'''
while(cap.isOpened()):
	ret, frame = cap.read()

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	frame = cv2.flip(frame,180)	#flipping frame 180 degree
	out.write(frame)	#saves image in color since we out.write frame
	cv2.imshow('frame', gray)

	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	

cap.release()
out.release()
cv2.destroyAllWindows()
