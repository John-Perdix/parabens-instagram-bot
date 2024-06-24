from PIL import Image, ImageDraw, ImageFont


def add_text (im, text, topleft, size, colour):
    font = ImageFont.truetype("./fonts/Montserrat-Black.ttf", size)
    draw = ImageDraw.Draw(im)
    draw.text(topleft, text, font=font, fill=colour)
    return im

if __name__ == "__main__":
    with Image.open("./images/firstImage.jpg") as im:
        im = add_text(im, "Hello World\n I'm Mona", (75,100), 20, (255,255,255))
        im.save("./save-images/AddText.jpg")
