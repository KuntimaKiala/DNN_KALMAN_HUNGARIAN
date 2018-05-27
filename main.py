# python2 main.py --prototxt MobileNetSSD_deploy.prototxt.txt --model MobileNetSSD_deploy.caffemodel
from detector import Detector
from correlation_filter import Correlation_filter
from tracker import Tracker
import numpy as np
import argparse
import cv2
from imutils.video import FPS
import time
from superposition import IOU
from trace import Trace
#tracker = Tracker(160, 30, 2, 100)


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--prototxt", required=True,
	help="path to Caffe 'deploy' prototxt file")
ap.add_argument("-m", "--model", required=True,
	help="path to Caffe pre-trained model")
ap.add_argument("-c", "--confidence", type=float, default=0.50,
	help="minimum probability to filter weak detections")
args = vars(ap.parse_args()) 

video = "data/Inria2.avi"
fvs = cv2.VideoCapture(video)
time.sleep(2.0)

if (fvs.isOpened() == False): 
	print("Error opening video stream or file")

objecto = Detector()

# Create Object Tracker
nb_frame = 5
tracker = Tracker(160, 50, 3, 0)
# Variables initialization
skip_frame_count = 0
track_colors = [(255, 0, 0), (0, 255, 0), 
				(0, 0, 255), (255, 255, 0),
				(0, 255, 255), (255, 0, 255),
				(255, 127, 255),(127, 0, 255), 
				(127, 0, 127)]

COLORS = [(255,0,0), (0,0,255), (0,255,0), (255,255,255), (255,0,255)]

BoolVal = True
count = 0
activate = False
step = 0
T = 1

div = 1
kfc = False
fail = True
corr_ = 0
fil_ = True
f_ = False

while  fvs.isOpened():
	retval , frame = fvs.read()
	

	if retval == True :
		(h, w) = frame.shape[:2]
		frame = frame[0:h, 0:int(w/div)]
		if fil_ is True and corr_ == 0 :
			a,centers, boundingbox = objecto.detector(frame, args["prototxt"], args["model"], args["confidence"])

		if len(centers) > 0 or BoolVal == False or corr_ < 3 :
			activate =  True
			BoolVal = False
			if  BoolVal == False  :
				sup =IOU(boundingbox)
				confirm = sup.control()
				if confirm == True :
					f_ = True



			if f_ == True and corr_ < 3 :
				kfc = True
				boxes_kcf = boundingbox

				
			else :
				kfc = False


			if kfc == True :
				KFC = Correlation_filter(frame, boxes_kcf )
				centers, fail, rect, frame= KFC.correlation_filter(fvs, frame, boxes_kcf,div)
				corr_ +=1
				activate =  True
				boxes_kcf = rect

				confirm = False
				if (fail == True or confirm == False) and corr_ == 3:
				
					kfc == False
					corr_ = 0
					
					f_ = False



		if activate == True  :
			Tracer = Trace(centers, tracker)
			Tracer.trace(frame)

		# Display the resulting tracking frame
		cv2.imwrite('/home/kuntima/Documents/SIGMA/StageGipsaLab2018/PythonScripts/DNN_HUNGARIAN/MOTA_DenisMichel/frames%i.png' %count, frame)

		cv2.imshow('Tracking', frame)

	count +=1

		

	if cv2.waitKey(25) & 0xFF == ord('q'):
				break
				# Break the loop

	if retval == False : 
		break
   
# When everything done, release the video capture object
fvs.release()

