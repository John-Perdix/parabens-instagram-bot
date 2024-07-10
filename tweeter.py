import tweepy
import keys

# Create the authentication object
auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)

# Create the API object
api = tweepy.API(auth)

# Define a function to send a tweet
def tweet(api, message, image_path):
  if image_path:
    api.update_status_with_media(status=message, filename=image_path)
  else:
    api.update_status(status=message)

  print("Tweeted successfully!")

# Send a tweet
tweet(api, "This was tweeted from Python!", "images/happy-party.png")