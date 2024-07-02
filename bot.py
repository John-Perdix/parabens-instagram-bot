import os
import time
from instagrapi import Client
from instagrapi.exceptions import ClientError, ChallengeRequired

import json
import sys
from datetime import date

# Read credentials from file
with open("credenciais3.txt", "r") as f:
    username, password = f.read().splitlines()

# Path to save the session
session_path = f"logs/{username}_session.json"

# Create a Client instance
client = Client()


# Function to attempt login with retry logic
def login_with_retry(client, username, password, session_path, retries=5, delay=60):
    for attempt in range(retries):
        try:
            if os.path.exists(session_path):
                client.load_settings(session_path)
                print("Loaded session")
                if client.user_id:
                    return True
            else:
                client.login(username, password)
                client.dump_settings(session_path)
                print("Login successful and session saved")
                return True
        except ChallengeRequired:
            code = input("Enter the 2FA code: ")
            client.challenge_code_handler = lambda username, choice: code
            client.complete_challenge()
            client.dump_settings(session_path)
            print("2FA challenge completed and session saved")
            return True
        except ClientError as e:
            if 'Please wait a few minutes before you try again' in str(e):
                print(f"Rate limit hit, retrying in {delay} seconds... (Attempt {attempt + 1}/{retries})")
                time.sleep(delay)
            else:
                print(f"Login failed: {e}")
                break
    return False




hashtag = "parabens"
num_medias = 20

def process_hashtag_medias(client, hashtag, num_medias, processed_file="images/processed_media_ids.txt"):
    print("Estanos na parte do coiso")
    today = date.today()
    medias = client.hashtag_medias_recent(hashtag, num_medias)
    
    # Load processed media IDs
    try:
        with open(processed_file, "r") as f:
            processed_media_ids = set(f.read().splitlines())
    except FileNotFoundError:
        processed_media_ids = set()
    
    # Filter posts taken after today and not processed yet
    posts_to_process = [post for post in medias if post.taken_at.date() >= today and post.id not in processed_media_ids]
    
    for i, media in enumerate(posts_to_process):
        # Like the post
        client.media_like(media.id)
        
        # Get more information about the media
        mediaInfo = client.media_info(media.id)
        owner = mediaInfo.user
        user_info = client.user_info(owner.pk)
        picture_url = user_info.profile_pic_url

        # Save the photo with a unique filename
        filename = f"images/insta_{i+1}"
        # Download the photo
        picture_data = client.photo_download_by_url(picture_url, filename)
        
        usernameUser = user_info.username
        description = mediaInfo.caption_text
        print(usernameUser)
        print(description)

        filenameTxt = f"info_insta/insta_{i+1}.json"

        # Create a dictionary to hold the data
        data = {
            "username": usernameUser,
            "description": description.encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding)
        }

        # Write the dictionary to a file as JSON
        with open(filenameTxt, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        # Add the media ID to the set of processed IDs
        processed_media_ids.add(media.id)

    # Save the updated set of processed media IDs back to the file
    with open(processed_file, "w") as f:
        f.write("\n".join(processed_media_ids))


# Attempt login with retry mechanism
if login_with_retry(client, username, password, session_path):
    print("Logged in successfully")
else:
    print("Failed to log in after multiple attempts.")
    
    
process_hashtag_medias(client, hashtag, num_medias)

client.logout()