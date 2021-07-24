import cv2
from random import randrange 
trained_face_data= cv2.CascadeClassifier('face.xml')

webcam=cv2.VideoCapture(0)

while True:
    s_F_R,frame = webcam.read()

    cordinates = trained_face_data.detectMultiScale(frame)
    for(x,y,w,h) in cordinates:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,254),3)
        
    cv2.imshow('Face detector',frame)
    key=cv2.waitKey(1)

    if key==81 or key==113:
        break;
