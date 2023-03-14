import cv2
from matplotlib import pyplot as plt

inputimg1='./Resource/rusianplate1.jpg'
inputimg2='./Resource/rusianplate2.jpg'
xml='./haarcascade github/haarcascade_russian_plate_number.xml'

img1 = cv2.imread(inputimg1)
img1Gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img1RGB = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

img2 = cv2.imread(inputimg2)
img2Gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
img2RGB = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

plateCascade = cv2.CascadeClassifier(xml)
numberPlates = plateCascade.detectMultiScale(img1Gray)
numberPlates2 = plateCascade.detectMultiScale(img2Gray)

if len(numberPlates) != 0:
    for (x, y, w, h) in numberPlates:
        plateRoi = img1RGB[y:y+h,x:x+w]
        plateRoi = cv2.blur(plateRoi,(15,15))
        img1RGB[y:y+h,x:x+w] = plateRoi

if len(numberPlates2) != 0:
    for (x, y, w, h) in numberPlates2:
        plateRoi = img2RGB[y:y+h,x:x+w]
        plateRoi = cv2.blur(plateRoi,(15,15))
        img2RGB[y:y+h,x:x+w] = plateRoi


plt.subplot(1,1,1)
plt.imshow(img1RGB)
plt.show()
plt.imshow(img2RGB)
plt.show()