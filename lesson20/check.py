#Importing libraries
import cv2
import pytesseract


#Loading image using OpenCV
img = cv2.imread('u.jpg')
print(img)
#Converting to text
text = pytesseract.image_to_string(img)

print(text)
