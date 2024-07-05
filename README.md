# Parabens Instagram Bot

Parabens Instagram Bot is a Python-based automation tool designed to interact with Instagram to automatically search posts based on a specific hashtag, download the profile picture from the person who posted the picture, add ornaments and post the picture with a birthday message. This bot is intended for giving automatic birthday messages to pthe users making use of LLM capabilities.

## Features

- **search**: Seaches posts based on the hashtag "parabens".
- **Auto-like**: Automatically likes posts based on the hashtag "parabens".
- **Downloads profile pictures**: Automatically downloads the profile pictures of the one who posted with the hashtag "parabens".
- **Downloads post's description**: Automatically downloads the profile pictures of the one who posted with the hashtag "parabens".
- **face detections**: Automatically detects faces in the picture.
- **Adds ornaments**: Adds ornaments to arround the faces detected.
- **Prompts gemini**: Prompts gemini based on the context of the post's description, making a birthday messange.
- **Auto-posts**: Posts the picture with the ornaments and uses the gemini response as the description.
- **Logging**: Maintains a log of all actions performed for transparency and review.


## Requirements

- Python 3.6 or higher
- `opencv` library
- `geminiai` library
- `instagrapi` library
- `tenor` library
- `json` library
- `requests` library
- An Instagram account

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/John-Perdix/parabens-instagram-bot.git
    cd parabens-instagram-bot
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required libraries:
    ```bash
    pip install opencv-python
    pip install geminiai
    pip install
    instagrapi
    pip install tenor-py
    pip installrequests
    ```

## Configuration

1. Open the `credenciais.txt` file and update the fields with your Instagram credentials and preferences. Example:
    ```txt
        "your_instagram_username",
        "your_instagram_password",
    ```


## Usage

To run the bot, execute the following command:
```bash
python mainScript.py
