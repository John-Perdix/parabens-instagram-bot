import datetime
from instagrapi import Client
from instagrapi.types import StoryMention, StoryMedia, StoryLink, StoryHashtag

with open("credenciais.txt", "r") as f:
    username, password = f.read().splitlines()

# Get today's date
today = datetime.date.today()
print(today)
client = Client()
client.login(username, password)

hashtag = "parabens"

medias = client.hashtag_medias_recent(hashtag, 20)

# Filter posts taken after today
posts_after_today = [post for post in medias if post.taken_at.date() >= today]


for i, media in enumerate(posts_after_today):
    # Like the post
    client.media_like(media.id)
    
    # Get more information about the media
    mediaInfo = client.media_info(media.id)
    #print(mediaInfo)
    

    owner = mediaInfo.user
    user_info = client.user_info(owner.pk)
    picture_url = user_info.profile_pic_url
    username = user_info.username
    print(username)
    # Save the photo with a unique filename
    filename = f"images/insta_{i+1}"
    # Download the photo
    picture_data = client.photo_download_by_url(picture_url, filename)
    
        
        
    #client.photo_upload_to_story(filename)

client.logout()

