import cv2
import numpy as np
import matplotlib.pyplot as plt

face_classifier = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalface_default.xml')
eye_classifier = cv2.CascadeClassifier('data/haarcascades/haarcascade_eye.xml')
fullbody_classifier = cv2.CascadeClassifier('data/haarcascades/haarcascade_fullbody.xml')

#detetar a cara
def detect_faces(img):
    face_img = img.copy()
    face_rect = face_classifier.detectMultiScale(face_img, scaleFactor=1.3, minNeighbors=5)
    
    #for (x, y, w, h) in face_rect:
     #   cv2.rectangle(face_img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
    return face_rect

#colocar objetos por cima da cabeça 
def object_above_head(img, face_rect, object_img):
    img_final = img.copy()
    objH, objW = object_img.shape[:2] #para ter o comprimento e a largura da imagem

    print(face_rect)#dimensões do retangulo da cara

    for (x, y, w, h) in face_rect:
        pos_x = int(x + w / 2 - objW / 2)#posicao x para a imagem
        pos_y = int(y - objH)#posicao y para a imagem

        #verificar se fica bem posicionado
        if pos_y < 0:
            pos_y = 0 
        if pos_x < 0:
            pos_x = 0  
        if pos_x + objW > img_final.shape[1]:
            pos_x = img_final.shape[1] - objW  
        if pos_y + objH > img_final.shape[0]:
            pos_y = img_final.shape[0] - objH 

        print(f"posições do objeto: ({pos_x}, {pos_y})")

        for i in range(objH):
            for j in range(objW):
                if object_img[i, j, 3] > 0:  # Check if the pixel is not transparent
                    img_final[pos_y + i, pos_x + j] = object_img[i, j, :3]
            
    return img_final

#detetar os olhos
def detect_eyes(img):
    eye_img = img.copy()
    eye_rect = eye_classifier.detectMultiScale(eye_img, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in eye_rect:
        cv2.rectangle(eye_img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
    return eye_img


#detetar o corpo
def detect_fullbody(img):
    fullbody_img = img.copy()
    fullbody_rect = fullbody_classifier.detectMultiScale(fullbody_img, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in fullbody_rect:
        cv2.rectangle(fullbody_img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    return fullbody_img

img = cv2.imread('images/secondImage.jpg')
object_img = cv2.imread('images/coroa.png', cv2.IMREAD_UNCHANGED) #para verificar a transparencia

img_copy1 = img.copy()
img_copy2 = img.copy()
img_copy3 = img.copy()

face_detection = detect_faces(img_copy1)
img_final = object_above_head(img, face_detection, object_img)
#eyes_and_face_detection = detect_eyes(face_detection)
#fullbody_detection = detect_fullbody(eyes_and_face_detection)

coroa_rgb = cv2.cvtColor(img_final, cv2.COLOR_BGR2RGB)

plt.imshow(coroa_rgb)
plt.axis('off')
plt.show()

cv2.imwrite('happyBirthday/detect_face_coroa5.png', img_final)

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
