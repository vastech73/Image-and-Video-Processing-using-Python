#Tutorial on video capture
#Colour video capture
#Set the frame size
import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while(True):
    #Capture fram-by-frame
    ret,  frame = cap.read()
    cap.set(3,320)
    print('Width is 320')
    cap.set(4,240)
    print('height is 240')

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()

cv2.destroyAllWindows()
