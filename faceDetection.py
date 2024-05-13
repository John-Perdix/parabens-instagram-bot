import cv2 

# Load an image using OpenCV
img = cv2.imread('firstImage.jpg')

# Display the image
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
