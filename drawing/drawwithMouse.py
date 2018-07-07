import cv2
import numpy as np
#displays the list of mouse events
#events = [i for i in dir(cv2) if 'EVENT' in i]
#print events

def drawCircle(event,x,y,flags,param):
	if event == cv2.EVENT_LBUTTONDBLCLK:
		cv2.circle(img,(x,y),100,(255,255,0),-1)

img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',drawCircle)

while(1):
	cv2.imshow('image', img)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cv2.destroyAllWindows()
