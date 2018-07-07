import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('sample.jpg', 0)
rimg = cv2.resize(img, (720,480))

rimg = cv2.medianBlur(rimg, 5)

ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
rth1 = cv2.resize(th1, (720,480))

th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,\
		cv2.THRESH_BINARY,11,2)
rth2 = cv2.resize(th2, (720,480))

th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
		cv2.THRESH_BINARY,11,2)
rth3 = cv2.resize(th3, (720,480))

titles = ['Original Image', 'Global Thresholding 127', 'Adaptive mean thresholding', 'Adaptive Gaussian thresholding']

images = [rimg, rth1, rth2, rth3]

for i in xrange(4):
	plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
	plt.title(titles[i])
	plt.xticks([]),plt.yticks([])
plt.show()

if cv2.waitKey(1) & 0xff == ord('q'):
	cv2.destroyAllWindows()
