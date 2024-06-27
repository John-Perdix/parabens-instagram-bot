from instagrapi import Client
import os
import glob

with open("credenciais2.txt", "r") as f:
    username, password = f.read().splitlines()

client = Client()
client.login(username, password)

# Specify the directory containing images
image_folder = 'happyBirthday'


# Use glob to find all image files with a specific extension (e.g., .jpg, .png)
image_files = glob.glob(os.path.join(image_folder, '*'))


# Loop through each image file
for i, image_file in enumerate(image_files):
    print(f"Processing image: {image_file}")
    
    filename_read = f"gemini_res/insta_{i+1}.txt"
    with open(filename_read, "r", encoding="utf-8") as f:
        data = f.read()
        
    client.photo_upload(image_file, data)
    os.remove(image_file)

client.logout()