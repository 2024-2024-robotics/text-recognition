import cv2
from PIL import Image
from pytesseract import pytesseract
import matplotlib.pyplot as plt

camera = cv2.VideoCapture(0)

image_path = "test1.jpg"

def grayscale(image):
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return grayscale
    
def tesseract():
    path_to_tesseract = "/usr/bin/tesseract"
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(Image.open(image_path), config='--psm 6')
    print(text)

    text_list = [char for char in text]
    element = 0

    while element <= len(text_list):

        try:
            int(text_list[element])
        except ValueError:
            text_list.pop(element)
        except IndexError:
            print("Index error.")

        element += 1

    coordinates = text_list

    print(coordinates)

    x_coord = coordinates[0]
    y_coord = coordinates[1]

    # I will have to ask what the third number is for -Noah
    # z_coord

while True:
    _, image = camera.read()
    cv2.imshow('Text detection', image)

    if cv2.waitKey(1) & 0xFF == ord('s'):      
        image = grayscale(image)
        cv2.imwrite('test1.jpg', image)
        tesseract()

    elif cv2.waitKey(1) & 0xFF == ord('q'):
        break