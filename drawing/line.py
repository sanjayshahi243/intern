import cv2
import numpy as np

#np.zeros implies that image is to be filled with zero color( black (0,0,0))
img = np.zeros((512,512,3), np.uint8)

#creates line on img from top left(0,0) coordinate to bottom right(511,511) coordinate with width of 5
img = cv2.line(img,(0,0),(511,511),(255,0,0),5)

img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

img = cv2.circle(img,(150,150), 50, (0,0,255),5)

img = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

#Defining array of coordinates
pts = np.array([[10,5],[20,30],[70,20],[50,60],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))

#Creating polygon from on img with array of coordinates pts, false implies if the 2 end and first coordinate need to join of not and color
img = cv2.polylines(img,[pts],False,(255,255,255))

#defining font for text
font = cv2.FONT_HERSHEY_SIMPLEX
#Wreiting on img Opencv, with coordinates of font type as defined and size 4 color white(255,255,255) and alias
cv2.putText(img,'OpenCV',(10,500),font,4,(255,255,255),2,cv2.LINE_AA)

while(1):
	cv2.imshow('image', img)
	if cv2.waitKey(1) & 0xff == ord('q'):
		break


