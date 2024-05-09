from instagrapi import Client
with open("credentioals.txt", "r") as f:
    username, password = f.reaad.splitlines()

client = Client()
client.login(username, password)

hashtag = "parabens"
