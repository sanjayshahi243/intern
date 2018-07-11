import cv2
import numpy as np

#loading xml files of Detection
facecascades = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
#eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

def detect_face(frame):
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
	
	#detecting faces
	faces = facecascades.detectMultiScale(gray, 1.3, 1)
	
	#drawing rectangle around face
	
	for (x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
		#roi_gray = gray[y:y+h, x:x+w]
		#roi_color = frame[y:y+h, x:x+w]

	return frame

while(cap.isOpened()):
	ret, frame = cap.read()
	
	displayFrame = detect_face(frame)
	#displayGray = detect_face(gray)
	
	cv2.imshow('frame',displayFrame)
	#cv2.imshow('gray',gray)

	if cv2.waitKey(1) & 0xff == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
