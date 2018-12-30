#importing libraries

import cv2
import pytesseract
import tensorflow as tf
import pytesseract
from skimage.io import imread
from keras.preprocessing import image

#reading the image
config = ('-l eng --oem 1 --psm 3')
img = cv2.imread('imagetext.jpg')
cv2.imshow('image', img) 
cv2.waitKey(0)
cv2.destroyAllWindows()
 
def detect(frame):
    try: 
       frame=cv2.imread("imagetext.jpg", cv2.IMREAD_COLOR)
    except IOError:
        pass
    print(frame)
    text = pytesseract.image_to_string(frame, config=config)
    print(text)
    data = detect(frame) 


#converting the image to string

text = pytesseract.image_to_string(frame, config=config)
print(text)


  
    