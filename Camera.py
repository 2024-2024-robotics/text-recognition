import cv2
from PIL import Image
import time

camera = cv2.VideoCapture(0)

def init():
    
    picture_taken = False

    while True:

        time.sleep(5) # This will not be necessary in the final product

        _, image = camera.read()
        cv2.imshow('Text Detection', image)
        
        picture_taken = True

        if picture_taken: 
            cv2.imwrite('image.png', image)
            break
        
    camera.release()
    cv2.destroyAllWindows()
