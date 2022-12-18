import time

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from mss import mss
import pytesseract as tess


def display_img(img):
    plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    plt.show()
    # cv.namedWindow("cv", 0)
    # cv.resizeWindow("cv", 1000, 1000)
    # cv.imshow("cv", img)
    # cv.waitKey()


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
            if_continue = img_handler(img)
            if not if_continue:
                break
            time.sleep(1)


def img_ocr(img) -> str:
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    result = tess.image_to_string(img)
    return result
