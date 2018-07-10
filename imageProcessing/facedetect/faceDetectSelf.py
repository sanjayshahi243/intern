import cv2
import numpy as np

#loading image 
img = cv2.imread('sample4.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#cv2.imshow('original', img)

#loading xml files
facecascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#detecting faces
faces = facecascade.detectMultiScale(gray, 1.3, 5)


for(x, y, w, h) in faces:
	cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
	roi_gray = gray[y:y+h, x:x+w]
	roi_color = img[y:y+h, x:x+w]

cv2.imshow('original', img)
if cv2.waitKey(0):
	cv2.destroyAllWindows()

