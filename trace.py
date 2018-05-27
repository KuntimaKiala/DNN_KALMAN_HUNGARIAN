'''
	File name         : trace.py
	File Description  : Kalman filter
	Author            : Kuntima Kiala MIGUEL
	Date created      : 02/14/2017
	Date last modified: 18/05/2017
	Python Version    : 2.7
''' 



import numpy as np
import cv2



track_colors = [(255, 0, 0), (0, 255, 0), 
				(0, 0, 255), (255, 255, 0),
				(0, 255, 255), (255, 0, 255),
				(255, 127, 255),(127, 0, 255), 
				(127, 0, 127)]


class Trace :


	def __init__(self, centers, tracker) :
		self.centers = centers 
		self.tracker = tracker


	def trace(self, frame) :
		self.frame = frame
		# Track object using Kalman Filter
		self.tracker.Update(self.centers)
		# For identified object tracks draw tracking line
		# Use various colors to indicate different track_id
		for i in range(len(self.tracker.tracks)):
			#print("trace",tracker.tracks[i].trace)
			if (len(self.tracker.tracks[i].trace) > 1):
				if (len(self.tracker.tracks[i].trace[0][0]) > 1) :
					line = 0
					#print("trace",tracker.tracks[i].trace)
					for j in range(len(self.tracker.tracks[i].trace)-1):
					# Draw trace line
						x1 = self.tracker.tracks[i].trace[j][line][0]
						y1 = self.tracker.tracks[i].trace[j][line][1]

						clr = self.tracker.tracks[i].track_id % 9
						#y = y1 - 15 if y1 - 15 > 15 else y1 + 15
						#center = (int((x1+x2)/2), int((y1+y2)/2))
						#cv2.rectangle(self.frame, (startX, startY), (endX, endY),self.COLORS[idx], 2)
						cv2.circle(self.frame, (int(x1),int(y1)), 5, track_colors[clr], thickness=5, lineType=8, shift=0)
						#y2 =tracker.tracks[i].trace[j][(j/(nb_frame/2)) -1][3]
						clr = self.tracker.tracks[i].track_id % 9
						#label = "id: {}  ".format(clr)
						#y = y1 - 15 if y1 - 15 > 15 else y1 + 15
						#y = int(y1) - 15 if int(y1)- 15 > 15 else int(y1) + 15
						#cv2.putText(frame, label, (int(x1), y-70),cv2.FONT_HERSHEY_SIMPLEX, 0.5, track_colors[clr], 2)
						line +=1
						if line > 1 :
							line = 0
							#print ("tracker", tracker.tracks[i].prediction, x1)