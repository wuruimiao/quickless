import matplotlib.pyplot as plt
import cv2 as cv


def display_img(img):
    plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    plt.show()


def display_img_by_name(img_path):
    img = cv.imread(img_path)
    display_img(img)
