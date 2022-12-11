import cv2 as cv

from utils.image import display_img, capture_screen


def handle_img(img):
    display_img(img)
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    display_img(img)
    ret, img = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
    display_img(img)

    for i in range(100, 200, 5):
        edges = cv.Canny(img, i, 200)
        display_img(edges)


def main():
    capture_screen(handle_img)
