import matplotlib.pyplot as plt
import cv2 as cv
from PIL import Image
from mss import mss
import numpy as np


def display_img(img):
    plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    plt.show()


def display_img_by_name(img_path):
    img = cv.imread(img_path)
    display_img(img)


def capture_screen(img_handler):
    mon = {'left': 0, 'top': 0, 'width': 3804, 'height': 2160}
    with mss() as sct:
        while True:
            cap = sct.grab(mon)
            img = Image.frombytes('RGB', (cap.width, cap.height), cap.rgb, )
            img = np.array(img)
            img = cv.cvtColor(img, cv.COLOR_RGB2BGR)
            img_handler(img)
