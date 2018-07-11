import os
import cv2
import numpy as np
from PIL import Image

recognizer = cv2.face.createLBPHFaceRecognizer()
path = "dataset"

def getImagesWithID(path):
	ImagePaths = [os.path.join(path,f) for f in os.listdir(path)] 
	faces = []
	ids = []

	for imagePath in ImagePaths:
		faceImg = Image.open(imagePath).convert('L');
		faceNp = np.array(faceImg, 'uint8')
		ID = int(os.path.split(imagePath)[-1].split('.')[1])
		faces.append(faceNp)
		ids.append(id)

		cv2.imshow("training", faceNp)
		cv2.waitKey(10)	

	return ids, faces

ids, faces = getImagesWithID(path)
recognizer.train(faces, np.array(ids)) 
recognizer.save('recognizer/trainingData.yml')
cv2.destroyAllWindow()