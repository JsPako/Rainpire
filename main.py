import numpy as np
import cv2
import time
from PIL import Image, ImageGrab
from pynput.mouse import Button, Controller


def mouseMove():
    original = mouse.position
    for x in range(80000):
        x = x + 1
        mouse.position = (135, 942)
        if x == 79999:
            mouse.position = (135, 942)
            mouse.press(Button.left)
            mouse.release(Button.left)
            break
    for x in range(8000):
        x = x + 1
        mouse.position = (135, 942)
        if x == 7999:
            mouse.position = original
            break


def colourMatch(masked_image):
    thresh = cv2.threshold(masked_image, 0, 255,
                           cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    pixels = cv2.countNonZero(thresh)
    if pixels >= 500:
        mouseMove()
    else:
        return True


def processImage(original_image):
    mask_Image = cv2.inRange(original_image, lower_range, upper_range)
    colourMatch(mask_Image)


mouse = Controller()
upper_range = np.array([60, 255, 255])
lower_range = np.array([20, 180, 180])
timer = 0

while timer < 15000000:
    timer = timer + 1
    if timer == 1:
        screen = np.array(ImageGrab.grab(bbox=(97, 927, 167, 957)))
        cv2.imshow('view', screen)
        rgb = cv2.cvtColor(screen, cv2.COLOR_BGR2HSV)
        processImage(rgb)
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break
    if timer > 14999999:
        timer = 0
