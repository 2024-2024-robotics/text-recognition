import cv2
from PIL import Image
from pytesseract import pytesseract

def tesseract():
    path_to_tesseract = "/usr/bin/tesseract"
    image_path = "processed image.png"
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(Image.open(image_path))

    # text = list(text)

    if '/' in text: 
        text = text.replace('/', '7')
    else:
        pass
    
    text = list(text)
    del text[3:len(text)]

    coordinate_string = ''.join(text) 

    print(coordinate_string)

tesseract()
