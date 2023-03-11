import cv2
import numpy as np

plate_cascade=cv2.CascadeClassifier('haarcascade_github/haarcascade_russian_plate_number.xml')
path = r'C:\Users\syari\Downloads\rusianplate2.jpg'
cap=cv2.imread(path)

while True:
    ret, frame=cap.read()
    tickmark=cv2.getTickCount()
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    plate=plate_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3)
    for x, y, w, h in plate:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 10)
        frame[y:y+h, x:x+w] = cv2.GaussianBlur(frame[y:y+h, x:x+w],(23, 23), 30)


    if cv2.waitKey(1)&0xFF==ord('q'):
        break
    fps=cv2.getTickFrequency()/(cv2.getTickCount()-tickmark)
    cv2.putText(frame, "FPS: {:05.2f}".format(fps), (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, 
    (255, 0, 0), 2)
    cv2.imshow('video', frame)
cap.release()
cv2.destroyAllWindows()