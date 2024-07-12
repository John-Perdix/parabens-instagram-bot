import cv2
import os
import glob
import random
import unicodedata
import numpy as np

face_classifier = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalface_default.xml')
eye_classifier = cv2.CascadeClassifier('data/haarcascades/haarcascade_eye.xml')
fullbody_classifier = cv2.CascadeClassifier('data/haarcascades/haarcascade_fullbody.xml')
animal_face_classifier = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalcatface.xml')

""" #detetar a cara
def detect_faces(img):
    face_img = img

    # Detect human faces
    face_rect = face_classifier.detectMultiScale(face_img, scaleFactor=1.3, minNeighbors=5)

    # Detect animal faces (replace 'animal_face_classifier' with your specific classifier)
    animal_rect = animal_face_classifier.detectMultiScale(face_img, scaleFactor=1.3, minNeighbors=5)

    # Combine detections (optional)
    all_rect = np.concatenate((face_rect, animal_rect), axis=0)

    return all_rect """
    
#detetar a cara
def detect_faces(img):
    face_img = img

    # Detect human faces
    face_rect = face_classifier.detectMultiScale(face_img, scaleFactor=1.3, minNeighbors=5)

    return face_rect

#colocar objetos na imagem 
def object_above_head(img, face_rect, object_img, object_img2, object_img3):
    img_final = img.copy()

    objH, objW = object_img.shape[:2] #para ter o comprimento e a largura do primeiro objeto

    objH2, objW2 = object_img2.shape[:2] #do segundo objeto

    objH3, objW3 = object_img3.shape[:2] #do terceiro

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

        #segundo enfeite
        positions2 = [
            (int(x + w), int(y + h)),  #direita
            (int(x - h), int(y + h ))  #esquerda
        ]
        
        for pos_x2, pos_y2 in positions2: 
        
            pos_x2 = max(0, min(pos_x2, img_final.shape[1] - objW2))
            pos_y2 = max(0, min(pos_y2, img_final.shape[0] - objH2))

            print(f"posições do objeto2: ({pos_x2}, {pos_y2})")

            for i in range(objH2):
                for j in range(objW2):
                    if object_img2[i, j, 3] > 0: 
                        if 0 <= pos_y2 + i < img_final.shape[0] and 0 <= pos_x2 + j < img_final.shape[1]:
                            img_final[pos_y2 + i, pos_x2 + j] = object_img2[i, j, :3]

        #terceiro enfeite

        positions3 = [
            (int(x + w), int(y - h)),  #direita
            (int(x - h), int(y - h ))  #esquerda
        ]
        
        for pos_x3, pos_y3 in positions3: 
        
            pos_x3 = max(0, min(pos_x3, img_final.shape[1] - objW3))
            pos_y3 = max(0, min(pos_y3, img_final.shape[0] - objH3))

            print(f"posições do objeto3: ({pos_x3}, {pos_y3})")

            for i in range(objH3):
                for j in range(objW3):
                    if object_img3[i, j, 3] > 0:  # Check if the pixel is not transparent
                        if 0 <= pos_y3 + i < img_final.shape[0] and 0 <= pos_x3 + j < img_final.shape[1]:
                            img_final[pos_y3 + i, pos_x3 + j] = object_img3[i, j, :3]
    return img_final

#adicionar texto à imagem
""" def add_text(img, text, position, font=cv2.FONT_HERSHEY_SIMPLEX, scale=0.5, color=(255, 255, 255), thickness=2):

    img_text = img.copy()

    cv2.putText(img_text, text, position, font, scale, color, thickness, lineType=cv2.LINE_AA)
    return img_text

#remover os acentos do txt
def remover_acentos(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    ) """

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

#caminho das imagens de enfeites acima da cabeça/hat
enfeite_hat = 'enfeites/hats'
enfeites_folder_hat = glob.glob(os.path.join(enfeite_hat, '*'))

#caminho das imagens de enfeites ao lado da cabeça/baloons
enfeite_baloons = 'enfeites/baloons'
enfeites_folder_baloons = glob.glob(os.path.join(enfeite_baloons, '*'))

#caminho das imagens de enfeites ao lado da cabeça/confety
enfeite_confety = 'enfeites/confety'
enfeites_folder_confety = glob.glob(os.path.join(enfeite_confety, '*'))

#dimensoes para enfeites
new_width = 40
new_height = 40

#caminho das imagens do insta
image_folder = 'images'
info_folder = 'info_insta'
output_folder = 'happyBirthday'
os.makedirs(output_folder, exist_ok=True)

# Use glob to find all image files with a specific extension (e.g., .jpg, .png)
image_files = glob.glob(os.path.join(image_folder, '*'))
info_files = glob.glob(os.path.join(info_folder, '*'))

""" def resize_with_aspect_ratio(image, new_width):
  height, width = image.shape[:2]
  aspect_ratio = float(width / height)

  if new_width > width:  # Only resize if necessary
    # Scale based on width
    new_height = int(new_width / aspect_ratio)
    return cv2.resize(image, (new_width, new_height))
  else:
    # Image is already smaller or equal to desired width, no resize needed
    return image


# Loop through each image file
for i, image_file in enumerate(image_files):
    print(f"Change image: {image_file}")
    img = cv2.imread(image_file)

    #escolher um enfeite para cada imagem
    enfeites_random_hat = random.choice(enfeites_folder_hat)
    object_img = cv2.imread(enfeites_random_hat, cv2.IMREAD_UNCHANGED) #para verificar a transparencia
    enfeites_random_resize_hat = resize_with_aspect_ratio(object_img, new_width)

    enfeites_random_baloon = random.choice(enfeites_folder_baloons)
    object_img2 = cv2.imread(enfeites_random_baloon, cv2.IMREAD_UNCHANGED)
    enfeites_random_resize_baloon = resize_with_aspect_ratio(object_img2, new_width)

    enfeites_random_confety = random.choice(enfeites_folder_confety)
    object_img3 = cv2.imread(enfeites_random_confety, cv2.IMREAD_UNCHANGED)
    enfeites_random_resize_confety = resize_with_aspect_ratio(object_img3, new_width)

    face_detection = detect_faces(img)


    
    # se não for detetada nenhuma cara
    if len(face_detection) == 0:
        print(f"nenhuma cara detetada {image_file}")
        os.remove(image_file)
        for j, gemini_file in enumerate(gemini_files):
            if i == j:
                os.remove(gemini_file)
        continue

    img_object = object_above_head(img, face_detection, enfeites_random_resize_hat, enfeites_random_resize_baloon, enfeites_random_resize_confety)

    #remover os enfeites usados
    os.remove(enfeites_random_hat)
    os.remove(enfeites_random_baloon)
    os.remove(enfeites_random_confety)

    #img_final = cv2.cvtColor(img_object, cv2.COLOR_BGR2RGB)

    output_file = os.path.join(output_folder, os.path.basename(image_file))
    cv2.imwrite(output_file, img_object)
    os.remove(image_file) """
    
    # Loop through each image file
for i, image_file in enumerate(image_files):
    print(f"Change image: {image_file}")
    img = cv2.imread(image_file)

    #escolher um enfeite para cada imagem
    enfeites_random_hat = random.choice(enfeites_folder_hat)
    object_img = cv2.imread(enfeites_random_hat, cv2.IMREAD_UNCHANGED) #para verificar a transparencia
    enfeites_random_resize_hat = cv2.resize(object_img, (new_width, new_height))

    enfeites_random_baloon = random.choice(enfeites_folder_baloons)
    object_img2 = cv2.imread(enfeites_random_baloon, cv2.IMREAD_UNCHANGED)
    enfeites_random_resize_baloon = cv2.resize(object_img2, (new_width, new_height))

    enfeites_random_confety = random.choice(enfeites_folder_confety)
    object_img3 = cv2.imread(enfeites_random_confety, cv2.IMREAD_UNCHANGED)
    enfeites_random_resize_confety = cv2.resize(object_img3, (new_width, new_height))

    face_detection = detect_faces(img)
    
    # se não for detetada nenhuma cara
    if len(face_detection) == 0:
        print(f"nenhuma cara detetada {image_file}")
        os.remove(image_file)
        for j, info_file in enumerate(info_files):
            if i == j:
                os.remove(info_file)
        continue

    img_object = object_above_head(img, face_detection, enfeites_random_resize_hat, enfeites_random_resize_baloon, enfeites_random_resize_confety)

    #remover os enfeites usados
    #os.remove(enfeites_random_hat)
    #os.remove(enfeites_random_baloon)
    #os.remove(enfeites_random_confety)
    
    #img_final = cv2.cvtColor(img_object, cv2.COLOR_BGR2RGB)

    output_file = os.path.join(output_folder, os.path.basename(image_file))
    cv2.imwrite(output_file, img_object)
    #os.remove(image_file)