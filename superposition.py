

import numpy as np

class IOU :

	def __init__(self, bounding_boxes) :

		self.boxes = bounding_boxes
		self.validation = False
		self.Confirmation =  False


	


	def control(self) :


		def iou(bb_test,bb_gt):
			"""
			Computes IUO between two bboxes in the form [x1,y1,x2,y2]
			"""
			s = 0
			xx1 = np.maximum(bb_test[0], bb_gt[0])
			yy1 = np.maximum(bb_test[1], bb_gt[1])
			xx2 = np.minimum(bb_test[2], bb_gt[2])
			yy2 = np.minimum(bb_test[3], bb_gt[3])
			w = np.maximum(0., xx2 - xx1)
			h = np.maximum(0., yy2 - yy1)
			wh = w * h
			o = wh / ((bb_test[2]-bb_test[0])*(bb_test[3]-bb_test[1])+ (bb_gt[2]-bb_gt[0])*(bb_gt[3]-bb_gt[1]) - wh)
			if o > 0 and o < 1 :
				self.validation = True
			return self.validation

		for i in range(len(self.boxes)) :
			if len(self.boxes) > 0 :
				for j in range(len(self.boxes)) :
					self.Confirmation =iou(self.boxes[i], self.boxes[j])
			else :
				self.Confirmation = False


		return self.Confirmation

####TESTE####
""""T = [(10,10,20,20), (20,20,30,30), (50,50,100,100), (50,50,100,100), (75,75,100,100)]
#T = []
S = IOU(T)
Z = S.control()

print (Z)"""