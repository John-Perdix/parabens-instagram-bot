import cv2
import os
import glob
import random

face_classifier = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalface_default.xml')
eye_classifier = cv2.CascadeClassifier('data/haarcascades/haarcascade_eye.xml')
fullbody_classifier = cv2.CascadeClassifier('data/haarcascades/haarcascade_fullbody.xml')

#detetar a cara
def detect_faces(img):
    face_img = img.copy()
    face_rect = face_classifier.detectMultiScale(face_img, scaleFactor=1.3, minNeighbors=5)
    
    return face_rect

#colocar objetos por cima da cabeça 
def object_above_head(img, face_rect, object_img, object_img2):
    img_final = img.copy()
    objH, objW = object_img.shape[:2] #para ter o comprimento e a largura do primeiro objeto

    objH2, objW2 = object_img2.shape[:2] #do segundo objeto

    for (x, y, w, h) in face_rect:
        pos_x = int(x + w / 2 - objW / 2)#posicao x para a imagem
        pos_y = int(y - objH)#posicao y para a imagem

        # Boundary check for the first object
        pos_x = max(0, min(pos_x, img_final.shape[1] - objW))
        pos_y = max(0, min(pos_y, img_final.shape[0] - objH))   

        print(f"posições do objeto1: ({pos_x}, {pos_y})")

        for i in range(objH):
            for j in range(objW):
                if object_img[i, j, 3] > 0:  # Check if the pixel is not transparent
                    if 0 <= pos_y + i < img_final.shape[0] and 0 <= pos_x + j < img_final.shape[1]:
                        img_final[pos_y + i, pos_x + j] = object_img[i, j, :3]

        positions2 = [
            (int(x + w), int(y + h)),  #direita
            (int(x - h), int(y + h ))  #esquerda
        ]
        
        for pos_x2, pos_y2 in positions2: 
            # Boundary check for the second object
            pos_x2 = max(0, min(pos_x2, img_final.shape[1] - objW2))
            pos_y2 = max(0, min(pos_y2, img_final.shape[0] - objH2))

            print(f"posições do objeto2: ({pos_x}, {pos_y})")

             # Apply the second object
            for i in range(objH2):
                for j in range(objW2):
                    if object_img2[i, j, 3] > 0:  # Check if the pixel is not transparent
                        if 0 <= pos_y2 + i < img_final.shape[0] and 0 <= pos_x2 + j < img_final.shape[1]:
                            img_final[pos_y2 + i, pos_x2 + j] = object_img2[i, j, :3]
    return img_final

#adicionar texto à imagem
def add_text(img, text, position, font=cv2.FONT_HERSHEY_SIMPLEX, scale=1, color=(255, 255, 255), thickness=2):

    img_text = img.copy()

    cv2.putText(img_text, text, position, font, scale, color, thickness, lineType=cv2.LINE_AA)
    return img_text

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

#caminho das imagens de enfeites acima da cabeça
images_enfeite = 'enfeites/acimaDaCabeca'
enfeites_folder = glob.glob(os.path.join(images_enfeite, '*'))

#caminho das imagens de enfeites ao lado da cabeça
images_enfeite2 = 'enfeites/baloes'
enfeites_folder2 = glob.glob(os.path.join(images_enfeite2, '*'))


#caminho das imagens do insta
image_folder = 'images'
output_folder = 'happyBirthday'
os.makedirs(output_folder, exist_ok=True)

# Use glob to find all image files with a specific extension (e.g., .jpg, .png)
image_files = glob.glob(os.path.join(image_folder, '*'))

# Loop through each image file
for i, image_file in enumerate(image_files):
    print(f"Change image: {image_file}")
    img = cv2.imread(image_file)

    #escolher um enfeite para cada imagem
    enfeites_random = random.choice(enfeites_folder)
    object_img = cv2.imread(enfeites_random, cv2.IMREAD_UNCHANGED) #para verificar a transparencia

    enfeites_random2 = random.choice(enfeites_folder2)
    object_img2 = cv2.imread(enfeites_random2, cv2.IMREAD_UNCHANGED)

    face_detection = detect_faces(img)
    img_object = object_above_head(img, face_detection, object_img, object_img2)

    filename_read = f"gemini_res/insta_{i+1}.txt"
    with open(filename_read, "r", encoding="utf-8") as f:
        data = f.read()

    text = data
    position = (50, 50)
    img_text = add_text(img_object, text, position)
    
    #img_final = cv2.cvtColor(img_object, cv2.COLOR_BGR2RGB)

    output_file = os.path.join(output_folder, os.path.basename(image_file))
    cv2.imwrite(output_file, img_text)
    #os.remove(image_file)
