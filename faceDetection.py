import cv2
import numpy as np

import matplotlib.pyplot as plt 

#Haar Cascade for face detection
face_classifier = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalface_defaullt.xml')
eye_classifier = cv2.CascadeClassifier('data/haarcascades/haarcascade_eye.xml')
fullbody_classifier = cv2.CascadeClassifier('data\haarcascades\haarcascade_fullbody.xml')
def detect_faces(img):

    face_img = img.copy()

    face_rect = face_classifier.detectMultiScale(face_img, scaleFactor = 1.3, minNeighbors = 5)
    
  #  if len(faces) == 0:
   #     return img
    
    for (x, y, w, h) in face_rect:
        cv2.rectangle(face_img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
    return face_img

def detect_eyes(img):

    eye_img = img.copy()

    eye_rect = eye_classifier.detectMultiScale(eye_img, scaleFactor = 1.3, minNeighbors = 5)

    for (x, y, w, h) in eye_rect:
        cv2.rectangle(eye_img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
    return eye_img

def detect_fullbody(img):

    fullbody_img = img.copy()

    fullbody_rect = fullbody_classifier.detectMultiScale(fullbody_img, scaleFactor = 1.3, minNeighbors = 5)

    for (x, y, w, h) in fullbody_rect:
        cv2.rectangle(fullbody_img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        return fullbody_img
    

img = cv2.imread('images/4Image.jpg')
img_copy1 = img.copy()
img_copy2 = img.copy()
img_copy3 = img.copy()

face_detection = detect_faces(img_copy3)
eyes_and_face = detect_eyes(face_detection)
eyes_face_and_fullbody = detect_fullbody(eyes_and_face)
plt.imshow(eyes_face_and_fullbody)
cv2.imwrite('eyes_face_and_fullbody.png', eyes_face_and_fullbody)

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# plt.subplot(1,1,1)
# plt.imshow(rgb)
# plt.show()


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
