import cv2
import numpy as np

from matplotlib import pyplot as plt

# Load the pre-trained Haar Cascade for face detection
# face_classifier = cv2.CascadeClassifier('data\haarcascades\haarcascade_frontalface_defaullt.xml')
img = cv2.imread('save-images/firstImage.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.subplot(1,1,1)
plt.imshow(rgb)
plt.show()
#def detect_faces(img):
    
 #   faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    
  #  if len(faces) == 0:
   #     return img
    
    #for (x, y, w, h) in faces:
     #   cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
    #return img

# Capture video from the default webcam
# cap = cv2.VideoCapture(1)

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         print("Failed to capture image")
#         break
    
#     frame = detect_faces(frame)
#     cv2.imshow('Video Face Detection', frame)

#     if cv2.waitKey(1) & 0xFF == ord('p'):
#         break

    
# Display the image
#cv2.imshow('Image', img)
#cv2.waitKey(0)

#cap.release()
#cv2.destroyAllWindows()
