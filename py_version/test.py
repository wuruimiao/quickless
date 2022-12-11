# from multiprocessing import Pool
# import time
#
# def test(i):
#     time.sleep(5)
#     print(i)
#
# def test1(i):
#     print(i)
#     sum = 0
#     for i in range(9999999999):
#         sum += i
#
# pool = Pool(processes=2)
# for i in range(4):
#     res = pool.apply_async(test1, (i, ))
#     #res.get()
#
# pool.close()
# pool.join()

# print(tess.get_tesseract_version())
# print(tess.get_languages())
import cv2 as cv
import pytesseract as tess

from controller.img_page import get_left_screen_page
from utils.image import display_img


# img = cv.imread("images/color1.png")
# img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# print(tess.image_to_string(img, lang="chi_sim"))
# print(tess.image_to_boxes(img, lang="chi_sim"))


def test(img):
    display_img(img)
    img = get_left_screen_page(img)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    result = tess.image_to_boxes(img, lang="chi_sim")
    print(result)
    display_img(img)


# capture_screen(test)
from controller.gui_thatwind_tool import get_tool_page_origin_link

print(get_tool_page_origin_link())
