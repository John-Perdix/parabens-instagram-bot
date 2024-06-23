from instagrapi import Client
import os
import glob

with open("credenciais.txt", "r") as f:
    username, password = f.read().splitlines()

client = Client()
client.login(username, password)

# Specify the directory containing images
image_folder = 'images'

# Use glob to find all image files with a specific extension (e.g., .jpg, .png)
image_files = glob.glob(os.path.join(image_folder, '*'))

# Loop through each image file
for image_file in image_files:
    print(f"Processing image: {image_file}")
    

    client.photo_upload_to_story(image_file)

client.logout()
