import cv2 
import numpy as np

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.sml')

def detect_faces(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    if faces is ():
        return img
    
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    return img

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = detect_faces(frame)

    cv2.imshow('Video Face Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
# # Load an image using OpenCV
# img = cv2.imread('firstImage.jpg')

# # Display the image
# cv2.imshow('Image', img)
# cv2.waitKey(0)
cv2.destroyAllWindows()
