import numpy as np
import cv2
import time
from PIL import Image, ImageGrab
from pynput.mouse import Button, Controller


def processImage(original_image):
    mask_Image = cv2.inRange(original_image, lower_range, upper_range)
    cv2.imshow('Mask', mask_Image)
    cv2.imshow('image', original_image)

upper_range = np.array([60, 255, 255])
lower_range = np.array([20, 70, 70])

while(True):
    #screen = np.array(ImageGrab.grab(bbox=(97, 927, 167, 957)))
    screen = cv2.imread("rain.png")
    rgb = cv2.cvtColor(screen, cv2.COLOR_BGR2HSV)
    processImage(rgb)
    if cv2.waitKey(25) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break
