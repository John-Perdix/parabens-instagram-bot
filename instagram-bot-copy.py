import datetime
from instagrapi import Client
import json
import sys
import io
import random
import time

# Set the default encoding to UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open("credenciais.txt", "r") as f:
    username, password = f.read().splitlines()

# Get today's date
today = datetime.date.today()
print(today)
client = Client()
client.login(username, password)

hashtag = "parabens"
medias = client.hashtag_medias_recent(hashtag, 20)
processed_file="processed_media/processed_media_ids.txt"

try:
    with open(processed_file, "r") as f:
        processed_media_ids = set(f.read().splitlines())
except FileNotFoundError:
    processed_media_ids = set()

# Filter posts taken after today
posts_after_today = [post for post in medias if post.taken_at.date() >= today]
posts_to_process = [post for post in medias if post.taken_at.date() >= today and post.id not in processed_media_ids]


for i, media in enumerate(posts_to_process):
    try:
        # Like the post
        client.media_like(media.id)
        randomDelay1 = random.randint(30, 120)  # Example: delay between 30 and 120 seconds
        print(f"Delay of {randomDelay1} seconds to prevent restrictions.")
        time.sleep(randomDelay1)
        
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
    except Exception as e:
        print(f"An error occurred while processing media {media.id}: {e}")
        
    randomDelay = random.randint(5, 25)
    print("Delay de "+ str(randomDelay) +"seconds, to prevent instagram restrictions")
    time.sleep(randomDelay)

# Save the updated set of processed media IDs back to the file
with open(processed_file, "w") as f:
    f.write("\n".join(processed_media_ids))
        

client.logout()

