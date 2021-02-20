import cv2
import pytesseract
from PIL import Image
import re

def im2txt(filename):
    image = cv2.imread(filename)
    gray = cv2.bitwise_not(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_TRUNC | cv2.THRESH_OTSU)[1]
    
    text = pytesseract.image_to_string(gray,lang ='eng')
    text = text.split('\n')
    for x,y in enumerate(text):
        if y == '':
            text.pop(x)
    text = '\n'.join(text)
    text = re.sub('[^A-Za-z0-9,.]+', ' ', text)
    return text

print(im2txt("sample1.jpg"))
