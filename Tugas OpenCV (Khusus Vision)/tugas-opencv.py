import cv2
import matplotlib.pyplot as plt

# Path declaration
input_path = './Resource/rusianplate1.jpg'
output_path = './output/blur-rusianplate1.jpg'
classifier_path = './haarcascade github/haarcascade_russian_plate_number.xml'

# Read image file
img = cv2.imread(input_path)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Declare classifier
plate_cascade = cv2.CascadeClassifier(classifier_path)
found = plate_cascade.detectMultiScale(img_gray)

# Blurring the image
if len(found) != 0:
    for (x, y, width, height) in found:
        img_rgb[y: y+height, x: x + width, :] = cv2.blur(img_rgb[y: y+height, x: x + width, :], (50,50))

# Preparing the plot and showing the image
plt.subplot(1,1,1)
plt.imshow(img_rgb)
plt.show()

# Write an output file
img_rgb = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB)
cv2.imwrite(output_path, img_rgb)