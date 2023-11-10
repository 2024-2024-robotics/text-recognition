import Camera # Takes picture
import Pre # Preprocesses image
import PrintText # Print the text after processing
import os
import time

Camera.init()

if os.path.exists('image.png'):
    Pre.init()
    time.sleep(1)

    PrintText.init()
