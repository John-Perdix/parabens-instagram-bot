from instagrapi import Client
from instagrapi.types import StoryMention, StoryMedia, StoryLink, StoryHashtag

with open("credenciais.txt", "r") as f:
    username, password = f.read().splitlines()

client = Client()
client.login(username, password)

user_id = client.user_id_from_username("specific_user_username")
stories = client.user_stories(user_id)


target_user_id = client.user_id_from_username(username)

tagged_stories = []
for story in stories:
    if story.usertags:
        for tag in story.usertags:
            if tag.user.pk == target_user_id:
                tagged_stories.append(story)
                break

# Output tagged stories
for story in tagged_stories:
    print(f"Story ID: {story.pk}, Timestamp: {story.taken_at}, URL: {story.media_url}")

""" 
for i, story in enumerate(tagged_stories):
    print(f"Story ID: {story.pk}")
    for mention in story.mentions:
        if mention.user.pk == user_id:
            # Like the post
            client.story_like(story.pk)
            
            # Get more information about the media
            mediaInfo = client.story_info(story.pk)
            #print(mediaInfo)
            

            owner = mediaInfo.user
            user_info = client.user_info(owner.pk)
            picture_url = story.story_info.url
            username = user_info.username
            print(username)
            # Save the photo with a unique filename
            filename = f"images/insta_{i+1}"
            # Download the photo
            picture_data = client.story_download_by_url(picture_url, filename)
            
            
            #client.photo_upload_to_story(filename) """

client.logout()

