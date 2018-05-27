'''
	File name         : correlation_filter.py
	File Description  : Kernelized Correlation Filter KCF
	Author            : Kuntima Kiala MIGUEL
	Date created      : 02/14/2017
	Date last modified: 18/05/2017
	Python Version    : 2.7
'''
import cv2
import dlib




class Correlation_filter :

	def __init__(self, frame, box) :
		
		self.box =  box
		self.frame =  frame
		self.centroids = []
		self.fail = False
		
		# Provide the tracker the initial position of the object
		#


	def correlation_filter(self, fvs, frame, box,div) :
		self.fvs  = fvs
		self.box = box
		self.frame = self.frame
		self.div = div
		self.tracker = [dlib.correlation_tracker() for _ in xrange(len(self.box))]
		[self.tracker[i].start_track(self.frame, dlib.rectangle(*rect)) for i, rect in enumerate(self.box)]
		Condition = True
		self.centroids = []
		iteration = 0
		self.boundingbox = []
		
		while iteration < 1 :


			
	
			retval, img = self.fvs.read()
			if retval == True :
				(h, w) = img.shape[:2]
				img = img[0:h, 0:int(w/self.div)]

				

				if cv2.waitKey(25) & 0xFF == ord('q'):
					break
					# Break the loop
			else: 
				print "Cannot capture frame device | CODE TERMINATION :( "
				exit()
				break

			for i in xrange(len(self.tracker)):
				valor = self.tracker[i].update(img)
				# Get the position of th object, draw a 
				# bounding box around it and display it.
				rect = self.tracker[i].get_position()
				pt1 = (int(rect.left()), int(rect.top()))
				pt2 = (int(rect.right()), int(rect.bottom()))			

				p1 = pt1[0]
				p2 = pt1[1]
				p3 = pt2[0]
				p4 = pt2[1]
				p5 =p1
				center = ((p1+p3)/2 , (p2+p4/2) )
				self.centroids.append(center)
				box = (p1,p2,p3,p4)
				self.boundingbox.append(box)

				
				
				cv2.rectangle(img, pt1, pt2, (0,0,255), 3)
				if valor  < 0 or valor > 30 :
					Condition  = False
					self.fail = True
					break
			if Condition ==False :
				iteration = 100
				break
			#cv2.imshow("Frame", img)

			iteration +=1 
			if iteration == 1 :
				self.fail = True
 		return self.centroids, self.fail, self.boundingbox, img

		
		







	