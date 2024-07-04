import requests
import json
import os
import random
from PIL import Image, ImageSequence
import cv2  # Import OpenCV library

# Specify the directory containing the images
folderCount = 'images'
folderSave = 'enfeites/hats'

# Offset to the requests of the if api
offset = random.randint(0, 100)

def count_files(directory):
    """Counts the number of files in a directory (non-recursively)."""
    return len(os.listdir(directory))

num_files = count_files(folderCount)
print(f"There are {num_files} files in the folder.")

# Set the apikey and limit
apikey = "LIVDSRZULELA"  # Test value
lmt = num_files

# Our test search
search_term = "birthday hat"
def requestGifs(search_term, folderSave):
    # Get the top GIFs for the search term
    r = requests.get(f"https://g.tenor.com/v1/search?q={search_term}&key={apikey}&limit={lmt}&searchfilter=sticker&random=true&pos={offset}")

    if r.status_code == 200:
        # Load the GIFs using the urls
        top_gifs = r.json()

        for gif_info in top_gifs["results"]:
            # Look for any image URL (replace with the appropriate key)
            image_url = gif_info.get("media")[0].get("gif_transparent").get("url")

            if image_url:
                # Extract filename from URL (modify if needed)
                filename = os.path.basename(image_url)

                # Download and save the image
                image_response = requests.get(image_url)
                if image_response.status_code == 200:
                    gif_path = os.path.join(folderSave, filename)
                    with open(gif_path, "wb") as f:
                        f.write(image_response.content)

                    # Convert GIF to PNG with transparency using Pillow
                    with Image.open(gif_path) as img:
                        for frame in ImageSequence.Iterator(img):
                            frame = frame.convert("RGBA")
                            png_path = os.path.join(folderSave, f"{filename[:-4]}.png")
                            frame.save(png_path, format="PNG")
                            print(f"Downloaded and converted image: {png_path}")
                            break  # Save only the first frame as PNG
                else:
                    print(f"Failed to download image: {image_url}")
    else:
        print("Error fetching GIFs")

requestGifs("birthday hat", "enfeites/hats")
requestGifs("birthday baloon", "enfeites/baloons")
requestGifs("confety", "enfeites/confety")