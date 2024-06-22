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


#for i, media in enumerate(medias):
#    mediaId = media.id
#    client.media_like(mediaId)
#    pictureUrl = media.url
#    pictureData = client.photo_download(pictureUrl)
#    with open("downloaded_picture.jpg", "wb") as f:
#        f.write(pictureData)
#        print("picture downloaded")
#    #print(f"liked post numer {i+1} of hashtag {hashtag}")


for i, media in enumerate(medias):
    # Like the post
    client.media_like(media.id)
    
    # Get more information about the media
    mediaInfo = client.media_info(media.id)
    #print(mediaInfo)
    

    owner = mediaInfo.user
    user_info = client.user_info(owner.pk)
    picture_url = user_info.profile_pic_url
    # Download the photo
    picture_data = client.photo_download_by_url(picture_url)
    
    # Save the photo with a unique filename
    filename = f"images/insta_{i+1}.jpg"
    with open(filename, "wb") as f:
        if isinstance(picture_data, bytes):
            f.write(bytearray(picture_data))
        else:
            try:
                # Assuming picture_data might be a path-like object
                picture_data = open(str(picture_data), 'rb').read()  # Open as binary and read bytes
                f.write(picture_data)
            except (OSError, TypeError):  # Handle potential exceptions
                print(f"Error downloading picture {filename}")

        print(f"Picture downloaded: {filename}")
        
    client.photo_upload_to_story(filename)

client.logout()

