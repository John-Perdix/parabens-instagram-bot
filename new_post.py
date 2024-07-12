from instagrapi import Client
import os
import glob
import time

def read_credentials(file_path):
    with open(file_path, "r") as f:
        return f.read().splitlines()

def get_files(image_folder):
    return glob.glob(os.path.join(image_folder, '*'))

def read_caption(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
    


def upload_photos(client, image_files, caption_files):
    for i, image_file in enumerate(image_files):
        print(f"Processing image: {image_file}")
        for j, caption in enumerate(caption_files):
            if i == j: 
                caption_file = caption
        try:
            caption = read_caption(caption_file)
            client.photo_upload(image_file, caption)
            #os.remove(image_file)
            print(f"Uploaded and removed image: {image_file}")
            time.sleep(60)  # Add a delay of 60 seconds between uploads
        except client.exceptions.FeedbackRequired:
            print("Action restricted by Instagram. Manual intervention required.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    username, password = read_credentials("credenciais/credenciais6.txt")
    client = Client()
    client.login(username, password)

    image_folder = 'happyBirthday'
    caption_folder = 'gemini_res'
    image_files = get_files(image_folder)
    caption_files = get_files(caption_folder)

    upload_photos(client, image_files, caption_files)
    
    client.logout()

if __name__ == "__main__":
    main()
