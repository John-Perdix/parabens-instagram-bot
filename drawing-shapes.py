from PIL import Image, ImageDraw 

def add_cross_to(im, colour):
    draw = ImageDraw.Draw(im)
    draw.line((0,0) + im.size, fill=colour)
    draw.line((0, im.size[1], im.size[0], 0), fill=colour)
    return im  

def add_rectangle_to(im, topleft, bottomright, colour):
    draw = ImageDraw.Draw(im)
    draw.rectangle((topleft, bottomright), fill=colour)
    return im

def add_square_to(im, topleft, size, colour):
    draw = ImageDraw.Draw(im)
    draw.rectangle((topleft, (topleft[0] + size, topleft[1] * size)), fill=colour)
    return im

def add_ellipse_to(im, topleft, bottomright, colour):
    draw = ImageDraw.Draw(im)
    draw.ellipse((topleft, bottomright), fill=colour)
    return im

def add_circle_to(im, topleft, size, colour):
    draw = ImageDraw.Draw(im)
    draw.ellipse((topleft, (topleft[0] + size, topleft[1] * size)), fill=colour)
    return im

if __name__ == "__main__":
    with Image.open("./images/firstImage.jpg") as im:
        im_cross = add_cross_to(im, (255,0,0))
        im_rectangle = add_rectangle_to(im,(50,50),(70,60),(0,255,0))
        im_square = add_square_to(im,(100,100), 50, (0,0,255))
        im_ellipse = add_ellipse_to(im,(60,70),(100,130),(255,255,0))
        im_circle = add_circle_to(im,(50,50), 300, (100,255,255))


        im_cross.save("./save-images/firstImageCross.jpg")
        im_rectangle.save("./save-images/firstImageRectangle.jpg")
        im_square.save("./save-images/firstImageSquare.jpg")
        im_ellipse.save("./save-images/firstImageEllipse.jpg")
        im_circle.save("./save-images/firstImageCircle.jpg")
        