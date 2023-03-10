import cv2
import os
from matplotlib import pyplot as plt

os.chdir("E:\ROBOTIIK\Learning-Week-Programming-2023\Tugas OpenCV (Khusus Vision)")


img_first = cv2.imread('./Resource/rusianplate1.jpg')
img_second = cv2.imread('./Resource/rusianplate2.jpg')


plate_cascade = cv2.CascadeClassifier('./haarcascade github/haarcascade_russian_plate_number.xml')


gray = cv2.cvtColor(img_first, cv2.COLOR_BGR2GRAY)
gray_second = cv2.cvtColor(img_second, cv2.COLOR_BGR2GRAY)


plates_first = plate_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
plates_second = plate_cascade.detectMultiScale(gray_second, scaleFactor=1.1, minNeighbors=5)


for (x, y, w, h) in plates_first:
    plate = img_first[y:y+h, x:x+w]
    blurred_plate = cv2.GaussianBlur(plate, (35,35), 0)
    img_first[y:y+h, x:x+w] = blurred_plate

for (x, y, w, h) in plates_second:
    plate = img_second[y:y+h, x:x+w]
    blurred_plate = cv2.GaussianBlur(plate, (35,35), 0)
    img_second[y:y+h, x:x+w] = blurred_plate


fig = plt.figure()

img_first = cv2.cvtColor(img_first, cv2.COLOR_BGR2RGB)
img_second = cv2.cvtColor(img_second, cv2.COLOR_BGR2RGB)

first = fig.add_subplot(2,1,1)
first.imshow(img_first,aspect="auto")

second = fig.add_subplot(2,1,2)
second.imshow(img_second,aspect = "auto")


plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

