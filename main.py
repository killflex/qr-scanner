# ------------------------------------------------------------------------------------------------
# Import

import cv2
import numpy as np
import webbrowser as webb
from pyzbar.pyzbar import decode
from PIL import Image

# ------------------------------------------------------------------------------------------------
# Set up the QRCode Scanner

cam = cv2.VideoCapture(0)
    
while True:
    _, frame = cam.read()
    cv2.imshow("QRScanner Cam", frame)
    
    decodedObject = decode(frame)    
    for obj in decodedObject:
        # print(obj.data.decode("ascii"))
        
        if len(obj) >= 1:
            webb.open(obj.data.decode('utf-8'))
            exit()
        
    if cv2.waitKey(1) == ord('q'):
        break