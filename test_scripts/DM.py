from instagrapi import Client

with open("credenciais.txt", "r") as f:
    username, password = f.read().splitlines()

# Login to Instagram
client = Client()
client.login(username, password)

# Recipient's Instagram user_ids and the message you want to send
recipient_user_ids = client.user_id_from_username("strava")  # Add recipient's user_ids here
message = "Want to see the moonlight?"

# Send direct message
client.direct_send(message, recipient_user_ids)

# Logout
client.logout()

print("Direct message sent successfully!")
