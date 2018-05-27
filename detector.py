'''
	File name         : detector.py
	File Description  : DNN detector
	Author            : Kuntima Kiala MIGUEL
	Date created      : 02/14/2017
	Date last modified: 18/05/2017
	Python Version    : 2.7
'''


import numpy as np
import cv2
import time
import copy

class Detector :


	def __init__(self) :

		# initialize the list of class labels MobileNet SSD was trained to
		# detect, then generate a set of bounding box colors for each class
		self.CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
			"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
			"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
			"sofa", "train", "tvmonitor"]

		self.COLORS = np.random.uniform(0, 255, size=(len(self.CLASSES), 3))

		# load our serialized model from disk

		print("[INFO] loading model...")

	

	
	def detector (self, frame, prototxt, model, confidence) :
		
		
	
		
		

		self.prototxt = prototxt
		self.model = model
		self.confidence = confidence
		self.net = cv2.dnn.readNetFromCaffe(self.prototxt, self.model)


		

		lixo = []
		centroids =[]
		boxes =[]
		(h, w) = frame.shape[:2]
		#print ("count",  h,w)
		self.img = frame
		
		#print ("count",  h,w, self.depth_img.shape, self.img.shape, frame.shape)
		blob = cv2.dnn.blobFromImage(cv2.resize(self.img, (300, 300)),
				0.007843, (300, 300), 127.5)
		#print ("count",  self.img.shape)
		# pass the blob through the network and obtain the detections and
		# predictions
		self.net.setInput(blob)
		detections = self.net.forward()
		# loop over the detections
		count = 0
		(h, w) = self.img.shape[:2]

		
		boundingbox = []
		for i in np.arange(0, detections.shape[2]):

			#measurement = np.dot(kalman.measurementMatrix, state) 
			# extract the confidence (i.e., probability) associated with
			# the prediction
		
			confidence = detections[0, 0, i, 2]
			#print ("count", count)
			count +=1 

			# filter out weak detections by ensuring the `confidence` is
			# greater than the minimum confidence
			if confidence > self.confidence :
				# extract the index of the class label from the
				# `detections`, then compute the (x, y)-coordinates of
				# the bounding box for the object

				#to detect only a person 
				
				  
				idx = int(detections[0, 0, i, 1])
				if idx == 15 :
					box = detections[0, 0, i, 3:7] * np.array([int(w), h, int(w), h])
					(startX, startY, endX, endY) = box.astype("int")
					#print (box, i, count, ids)
					# draw the prediction on the frame
					#label = "{}: {:.2f}% ".format(self.CLASSES[idx],
					#confidence * 100)
					Y_ = endY -endX
					X_ = endX-startX
					pt1 = (startX + endX)/2 #Y
					pt2 = (startY + endY)/2 #X
					#radius = 1
					center = (pt1,pt2)
					X1 = startX
					Y1 = startY
					X2 = endX
					Y2 = endY
					#print (pt1,pt2, startX, startY, endX, endY, self.img.shape, center)
					#cv2.circle(self.frame, center, radius, self.COLORS[5], thickness=5, lineType=8, shift=0)
					cv2.rectangle(self.img, (X1, Y1), (X2, Y2),self.COLORS[idx], 2)
					
					#y = startY - 15 if startY - 15 > 15 else startY + 15
					#cv2.putText(self.frame, label, (startX, y),cv2.FONT_HERSHEY_SIMPLEX, 0.5, self.COLORS[idx], 2)
					centroids.append(center)
					bx = (startX, startY, endX, endY)
					box = (X1,Y1,X2,Y2)
					X = (X2+X1)/2
					Y = (Y2+Y1)/2
					
					cen = (int(X), int(Y))
					lixo.append(cen)
					#print "Center", center, centroids, self.depth_img.shape, X, Y
					boxes.append(center)
	
					

					boundingbox.append(bx)

			
				
		cv2.imshow("RGB Frame", self.img)
	


		
		return centroids, lixo, boundingbox


	



