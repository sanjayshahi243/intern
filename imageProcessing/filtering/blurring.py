import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('sample.jpg', 1)
rimg = cv2.resize(img, (720,480))

kernel = np.ones((5,5), np.float32)/50
dst = cv2.filter2D(rimg, 0, kernel)

plt.subplot(121),plt.imshow(rimg),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()

