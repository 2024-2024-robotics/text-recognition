import cv2
from PIL import Image

camera = cv2.VideoCapture(0)

while True:
    _, image = camera.read()
    cv2.imshow('Text Detection', image)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite('image.png', image)
        break
        
camera.release()
cv2.destroyAllWindows()
