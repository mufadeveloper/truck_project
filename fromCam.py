import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 640) #WIDTH
cap.set(4, 480) #HEIGHT
KNOWN_DISTANCE = 24.0 #inches


KNOWN_WIDTH = 640.0
focalLength = 3.04

face_cascade = cv2.CascadeClassifier("tranined_model.xml")


def distance_to_camera(knownWidth, focalLength, perWidth):
	return (knownWidth * focalLength) / perWidth

def Notify():
    print("Face detected............")


while(True):
    try:

        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
             cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

             roi=frame[y: y + h, x: x + w]
             marker = ((x,y),(x+w,y+h))

             inches = distance_to_camera(KNOWN_WIDTH, focalLength, marker[1][0])
             meter=inches*0.0254
             KNOWN_DISTANCE=inches

             if(meter<0.0):
                   cv2.putText(frame, "%.2fM" % (meter),
                         (frame.shape[1] - 200, frame.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,
                         2.0, (0, 255, 0), 3)
             

                   Notify()

        cv2.imshow('Result',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    except Exception as e:
        print("Reading frame.....")
        print(str(e))

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()







