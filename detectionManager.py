#!/usr/bin/env python
#-*- coding: utf-8 -*-

import cv
import time
import Image

#Declaracion de variables


class detectionManager:
    """
    Core de deteccion de rostros y manos, para pyranha
    """    
    def __init__(self):
        self.capture = cv.CreateCameraCapture(0)#camara con la que se captura, puede ir de 0 a n dependiendo de la cantidad de camaras
        self.width = None #en none va a auto detectar el tamaño 
        self.height = None #en none va a auto detectar el tamaño 
        self.faceCascade = cv.Load("haarcascades/haarcascade_frontalface_alt.xml")
        self.eyeCascade = cv.Load("haarcascades/haarcascade_eye.xml")
        self.handCascade = cv.Load("haarcascades/cascade.xml")
        self.Size()
        #self.detection()
        

    def Size(self):
        """
        Setea los valores para el tamaño de la ventana asociada al capturador de video
        """
        if self.width is None:
            self.width = int(cv.GetCaptureProperty(self.capture, cv.CV_CAP_PROP_FRAME_WIDTH))
        else:
            cv.SetCaptureProperty(self.capture,cv.CV_CAP_PROP_FRAME_WIDTH,self.width)    
        if self.height is None:
            self.height = int(cv.GetCaptureProperty(self.capture, cv.CV_CAP_PROP_FRAME_HEIGHT))
        else:
            cv.SetCaptureProperty(self.capture,cv.CV_CAP_PROP_FRAME_HEIGHT,self.height) 

        result = cv.CreateImage((self.width,self.height),cv.IPL_DEPTH_8U,3)
        return result
        
    def Load(self):
        """
        Carga los haar necesarios para la deteccion de rotros y ojos
        """
        return (faceCascade, eyeCascade, handCascade)

    def DetectEyes(self,image, faceCascade, eyeCascade, handCascade):
	    min_size = (20,20)
	    image_scale = 2
	    haar_scale = 1.2
	    min_neighbors = 2
	    haar_flags = 0

	    # Guardado temporal de las imagenes
	    gray = cv.CreateImage((image.width, image.height), 8, 1)
	    smallImage = cv.CreateImage((cv.Round(image.width / image_scale),cv.Round (image.height / image_scale)), 8 ,1)

	    # Convierte la imagen a escala de grises
	    cv.CvtColor(image, gray, cv.CV_BGR2GRAY)

	    # Rescala la imagen, a una mas pequeña para procesarla mas rapido
	    cv.Resize(gray, smallImage, cv.CV_INTER_LINEAR)

	    # Ecualiza el histograma
	    cv.EqualizeHist(smallImage, smallImage)

	    # Usa el xml y la lectura de la camara reducida
	    faces = cv.HaarDetectObjects(smallImage, faceCascade, cv.CreateMemStorage(0), haar_scale, min_neighbors, haar_flags, min_size)
            hands = cv.HaarDetectObjects(smallImage, handCascade, cv.CreateMemStorage(0), haar_scale, min_neighbors, haar_flags, min_size)
	    # Si se detectan rostros
	    if hands:
		    print ("Detecto una mano")
		    for ((x, y, w, h), n) in hands:
		    #the input to cv.HaarDetectObjects was resized, so scale the
		    #bounding box of each face and convert it to two CvPoints
			    pt1 = (int(x * image_scale), int(y * image_scale))
			    pt2 = (int((x + w) * image_scale), int((y + h) * image_scale))
			    cv.Rectangle(image, pt1, pt2, cv.RGB(255, 0, 0), 3, 8, 0)
			    face_region = cv.GetSubRect(image,(x,int(y + (h/4)),w,int(h/2)))

		    cv.SetImageROI(image, (pt1[0],pt1[1], pt2[0] - pt1[0], int((pt2[1] - pt1[1]) * 0.7)))
		    #eyes = cv.HaarDetectObjects(image, eyeCascade,cv.CreateMemStorage(0),haar_scale, min_neighbors,haar_flags, (15,15))
                    """
		    if eyes:
			    print("detecto ojos bellisimos")
			    # por cada ojo detectado
			    for eye in eyes:
				    # Dibuja un rectangulo al rededor del ojo
				    cv.Rectangle(image,
				    (eye[0][0],
				    eye[0][1]),
				    (eye[0][0] + eye[0][2],
				    eye[0][1] + eye[0][3]),
				    cv.RGB(15, 133, 224), 1, 8, 0)
                    """
            else:
	        print ("no detecta nada")
	    cv.ResetImageROI(image)
	    return image
        
        
    def detection(self):
        while True:
	    #capturando video
	    img = cv.QueryFrame(self.capture)
	    image = self.DetectEyes(img,self.faceCascade,self.eyeCascade,self.handCascade)
	    #cv.ShowImage("camera", image)
	    k = cv.WaitKey(10);
	    if k == 'f':
		break    
        return True

#===============================================================================#
#def main():
    """
    Main
    """
#    dm = detectionManager()
#    dm.detection()
    
    
#if __name__=='__main__':
#    main()
#===============================================================================#
