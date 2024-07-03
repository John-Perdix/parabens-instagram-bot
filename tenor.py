import requests
import json
import os
import random

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

# Get the top 8 GIFs for the search term
r = requests.get(
    "https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s&offset=%s" % (search_term, apikey, lmt, offset))

if r.status_code == 200:
    # Load the GIFs using the urls
    top_8gifs = json.loads(r.content)

    import cv2  # Import OpenCV library

    for gif_info in top_8gifs["results"]:
        # Look for any image URL (replace with the appropriate key)
        image_url = gif_info.get("beststatic_url")
        if not image_url:
            image_url = gif_info.get("url")

        if image_url:
            # Extract filename from URL (modify if needed)
            filename = os.path.basename(image_url)

            # Download and save the image
            image_response = requests.get(image_url)
            if image_response.status_code == 200:
                with open(os.path.join(folderSave, filename), "wb") as f:
                    f.write(image_response.content)

                # Read the downloaded image using OpenCV
                img = cv2.imread(os.path.join(folderSave, filename), cv2.IMREAD_UNCHANGED)

                # Check if image read successfully
                if img is not None:
                    # Save the image as PNG using OpenCV
                    cv2.imwrite(os.path.join(folderSave, f"{filename[:-4]}.png"), img)
                    print(f"Downloaded image: {filename[:-4]}.png")
                else:
                    print(f"Failed to read image: {filename}")
else:
    print("Error fetching GIFs")
