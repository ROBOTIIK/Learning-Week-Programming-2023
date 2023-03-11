import cv2

NumPlateCascade = cv2.CascadeClassifier('haarcascade_github/haarcascade_russian_plate_number.xml')

cap = cv2.VideoCapture('haarcascade_github/rusianplate2.mp4')

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 80)


if (cap.isOpened()==False):
    print('Error Reading video!!!')

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    NumPlate = NumPlateCascade.detectMultiScale(gray,scaleFactor=1.2,
    minNeighbors = 5, minSize=(25,25))

    for (x,y,w,h) in NumPlate:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        Numberplate = frame[y:y+h, x:x+w,:]
        Numberplate_to_be_shown_up = frame[y:y+h, x:x+w,:]
        Numberplate = cv2.blur(Numberplate, ksize=(50, 50))
        frame[:h,-w:,:] = Numberplate_to_be_shown_up
        frame[y:y+h, x:x+w,:] = Numberplate
    if ret == True:
        cv2.imshow('Video',frame)
    
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    
    else:
        break

cap.release()
cv2.destroyAllWindows()