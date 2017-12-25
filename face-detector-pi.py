import cv2
import os
import pygame, sys

width = 640
height = 480

#initialise pygame
pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0",(width,height))
cam.start()

#cap = cv2.VideoCapture("test_vid.mp4")
#cap.set(3, 640) #WIDTH
#cap.set(4, 480) #HEIGHT

face_cascade = cv2.CascadeClassifier("tranined_model.xml")


def Notify():
    print("Face detected............")


windowSurfaceObj = pygame.display.set_mode((width,height),1,16)
pygame.display.set_caption('Camera')

while(True):
  #take a picture
    image = cam.get_image()
    #display the picture
    catSurfaceObj = image
    windowSurfaceObj.blit(catSurfaceObj,(0,0))
    pygame.display.update()
  # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Display the resulting frame
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        Notify()

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.stop()
cv2.destroyAllWindows()