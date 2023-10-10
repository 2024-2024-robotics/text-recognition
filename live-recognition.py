import cv2
from PIL import Image
from pytesseract import pytesseract

camera = cv2.VideoCapture(0)

def tesseract():
    path_to_tesseract = "/usr/bin/tesseract"
    image_path = "test1.jpg"
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(Image.open(image_path))
    print(text)

while True:
    _, image = camera.read()
    cv2.imshow('Text detection', image)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        tesseract()
        cv2.imwrite('test1.jpg', image)
        break
        
camera.release()
cv2.destroyAllWindows()
