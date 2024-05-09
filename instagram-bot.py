import datetime
from instagrapi import Client
with open("credenciais.txt", "r") as f:
    username, password = f.read().splitlines()

# Get today's date
today = datetime.date.today()
client = Client()
client.login(username, password)

hashtag = "parabens"

medias = client.hashtag_medias_recent(hashtag, 20)

# Filter posts taken after today
posts_after_today = [post for post in medias if post.taken_at.date() >= today]


for i, media in enumerate(posts_after_today):
    client.media_like(media.id)
    print(f"liked post numer {i+1} of hashtag {hashtag}")

