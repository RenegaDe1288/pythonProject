import pytesseract
import cv2
import matplotlib.pyplot as plt
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

#Loading image using OpenCV
img = Image.open('index.png')
conf = r'--oem 3 --psm 13'
#Applying image_to_string method
text = pytesseract.image_to_string(img,config=conf)

print(text)
for i in text:
    if i.isdigit():
        print(i,end='')
print(type(text))
