#!/usr/bin/env python
#-*- coding: utf-8 -*-

import cv
import time
import Image

#Declaracion de variables


class detectionManager:
  
     
    def __init__(self):
        capture = cv.CreateCameraCapture(0)#camara con la que se captura, puede ir de 0 a n dependiendo de la cantidad de camaras
        width = None #en none va a auto detectar el tamaño 
        height = None #en none va a auto detectar el tamaño 
        faceCascade = cv.Load("/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml")
        eyeCascade = cv.Load("/usr/share/opencv/haarcascades/haarcascade_eye.xml")
        Size()
        detection()

    def Size(self):
        if width is None:
            width = int(cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_WIDTH))
        else:
            cv.SetCaptureProperty(capture,cv.CV_CAP_PROP_FRAME_WIDTH,width)    
        if height is None:
            height = int(cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_HEIGHT))
        else:
            cv.SetCaptureProperty(capture,cv.CV_CAP_PROP_FRAME_HEIGHT,height) 

        result = cv.CreateImage((width,height),cv.IPL_DEPTH_8U,3)
        return result
        
    def Load(self):
        return (faceCascade, eyeCascade)

    def Display(image):
        cv.NamedWindow("Red Eye Test")
        cv.ShowImage("Red Eye Test", image)
        cv.WaitKey(0)
        cv.DestroyWindow("Red Eye Test")

    def DetectRedEyes(image, faceCascade, eyeCascade):
	    min_size = (20,20)
	    image_scale = 2
	    haar_scale = 1.2
	    min_neighbors = 2
	    haar_flags = 0

	    # Allocate the temporary images
	    gray = cv.CreateImage((image.width, image.height), 8, 1)
	    smallImage = cv.CreateImage((cv.Round(image.width / image_scale),cv.Round (image.height / image_scale)), 8 ,1)

	    # Convert color input image to grayscale
	    cv.CvtColor(image, gray, cv.CV_BGR2GRAY)

	    # Scale input image for faster processing
	    cv.Resize(gray, smallImage, cv.CV_INTER_LINEAR)

	    # Equalize the histogram
	    cv.EqualizeHist(smallImage, smallImage)

	    # Usa el xml y la lectura de la camara reducida
	    faces = cv.HaarDetectObjects(smallImage, faceCascade, cv.CreateMemStorage(0),
	    haar_scale, min_neighbors, haar_flags, min_size)

	    # If faces are found
	    if faces:
		    print ("Detecto una cara linda")
		    for ((x, y, w, h), n) in faces:
		    # the input to cv.HaarDetectObjects was resized, so scale the
		    # bounding box of each face and convert it to two CvPoints
			    pt1 = (int(x * image_scale), int(y * image_scale))
			    pt2 = (int((x + w) * image_scale), int((y + h) * image_scale))
			    cv.Rectangle(image, pt1, pt2, cv.RGB(255, 0, 0), 3, 8, 0)
			    face_region = cv.GetSubRect(image,(x,int(y + (h/4)),w,int(h/2)))

		    cv.SetImageROI(image, (pt1[0],
			    pt1[1],
			    pt2[0] - pt1[0],
			    int((pt2[1] - pt1[1]) * 0.7)))
		    eyes = cv.HaarDetectObjects(image, eyeCascade,
		    cv.CreateMemStorage(0),
		    haar_scale, min_neighbors,
		    haar_flags, (15,15))	

		    if eyes:
			    print("detecto ojos bellisimos")
			    # For each eye found
			    for eye in eyes:
				    # Draw a rectangle around the eye
				    cv.Rectangle(image,
				    (eye[0][0],
				    eye[0][1]),
				    (eye[0][0] + eye[0][2],
				    eye[0][1] + eye[0][3]),
				    cv.RGB(15, 133, 224), 1, 8, 0)

	    cv.ResetImageROI(image)
	    return image
        
        
    def detection(self):
        while True:
	    #capturando video
	    img = cv.QueryFrame(capture)
	    #cv.Smooth(img,result,cv.CV_GAUSSIAN,9,9)
	    #cv.Dilate(img,result,None,5)
	    #cv.Erode(img,result,None,1)
	    #cv.Smooth(img,result,cv.CV_GAUSSIAN)
	    image = DetectRedEyes(img,faceCascade,eyeCascade)
	    cv.ShowImage("camera", image)
	    k = cv.WaitKey(10);
	    if k == 'f':
		break    
        return True

def main():
    """
    Main
    """
    dm = detectionManager()
    
    
if __name__=='__main__':
    main()