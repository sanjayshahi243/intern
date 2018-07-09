import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('sample.jpg',1)
rimg = cv2.resize(img, (720,480))
edges = cv2.Canny(img,10,200)
redges = cv2.resize(edges, (720,480))

cv2.imshow('original', rimg)
cv2.imshow('canny edges', redges)

'''plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()
'''

k = cv2.waitKey(0)
if k == 27:
# wait for ESC key to exit
	cv2.destroyAllWindows()
