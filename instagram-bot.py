import datetime
from instagrapi import Client
with open("credenciais.txt", "r") as f:
    username, password = f.read().splitlines()

# Get today's date
today = datetime.date.today()
client = Client()
client.login(username, password)

hashtag = "parabens"

medias = client.hashtag_medias_recent(hashtag, 3)

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
    media_info = client.media_info(media.id)
    
    # Get the URL of the photo
    if media_info.media_type == 1:  # 1 represents photo media type
        picture_url = media_info.urls[0]
        
        # Download the photo
        picture_data = client.photo_download(picture_url)
        
        # Save the photo with a unique filename
        filename = f"insta_{i+1}.jpg"
        with open(filename, "wb") as f:
            f.write(picture_data)
            print(f"Picture downloaded: {filename}")
    else:
        print(f"Media {media.id} is not a photo.")

client.logout()


client.logout()

