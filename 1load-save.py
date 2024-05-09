from PIL import Image

if __name__ == "__main__": 
    with Image.open("./images/firstImage.jpg") as im: 
        print(im.size)
        im.save("./save-images/firstImage.png")