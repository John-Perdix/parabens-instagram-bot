import datetime
import time
from instagrapi import Client
from instagrapi.exceptions import ClientError, ChallengeRequired
from instagrapi.types import StoryMention, StoryMedia, StoryLink, StoryHashtag
import json
import sys
import io
import os

# Set the default encoding to UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open("credenciais.txt", "r") as f:
    username, password = f.read().splitlines()

# Get today's date
today = datetime.date.today()
print(today)

# Path to save the session
session_path = f"{username}_session.json"

# Create a Client instance
client = Client()

# Function to attempt login with retry on rate limit
def login_with_retry(client, username, password, session_path, retries=5, delay=60):
    for attempt in range(retries):
        try:
            if os.path.exists(session_path):
                client.load_settings(session_path)
                print("Loaded session")
                return True
            else:
                client.login(username, password)
                client.dump_settings(session_path)
                print("Login successful and session saved")
                return True
        except ChallengeRequired as e:
            code = input("Enter the 2FA code: ")
            client.challenge_code_handler = lambda username, choice: code
            client.complete_challenge()
        except ClientError as e:
            if 'Please wait a few minutes before you try again' in str(e):
                print(f"Rate limit hit, retrying in {delay} seconds... (Attempt {attempt + 1}/{retries})")
                time.sleep(delay)
            else:
                print(f"Login failed: {e}")
                break
    return False

# Attempt login with retry mechanism
if login_with_retry(client, username, password, session_path):
    hashtag = "parabens"
    medias = client.hashtag_medias_recent(hashtag, 20)

    # Filter posts taken after today
    posts_after_today = [post for post in medias if post.taken_at.date() >= today]

    for i, media in enumerate(posts_after_today):
        # Like the post
        client.media_like(media.id)
        
        # Get more information about the media
        mediaInfo = client.media_info(media.id)
        owner = mediaInfo.user
        user_info = client.user_info(owner.pk)
        picture_url = user_info.profile_pic_url

        # Save the photo with a unique filename
        filename = f"images/insta_{i+1}.jpg"
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

    client.logout()
else:
    print("Failed to log in after multiple attempts.")
