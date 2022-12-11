import logging
import operator
from collections import defaultdict

import cv2 as cv

logger = logging.getLogger(__name__)


def _is_black(point) -> bool:
    return 0 <= point[0] <= 180 and \
           0 <= point[1] <= 255 and \
           0 <= point[2] <= 46


def _is_gray(point) -> bool:
    return 0 <= point[0] <= 180 and \
           0 <= point[1] <= 43 and \
           46 <= point[2] <= 220


def _is_white(point) -> bool:
    return 0 <= point[0] <= 180 and \
           0 <= point[1] <= 30 and \
           221 <= point[2] <= 255


def _is_red(point) -> bool:
    return 0 <= point[0] <= 10 or 156 <= point[0] <= 180 and \
           43 <= point[1] <= 255 and \
           46 <= point[2] <= 255


def _is_orange(point) -> bool:
    return 11 <= point[0] <= 25 and \
           43 <= point[1] <= 255 and \
           46 <= point[2] <= 255


def _is_yellow(point) -> bool:
    return 26 <= point[0] <= 34 and \
           43 <= point[1] <= 255 and \
           46 <= point[2] <= 255


def _is_green(point) -> bool:
    return 35 <= point[0] <= 77 and \
           43 <= point[1] <= 255 and \
           46 <= point[2] <= 255


def _is_deep_blue(point) -> bool:
    return 78 <= point[0] <= 99 and \
           43 <= point[1] <= 255 and \
           46 <= point[2] <= 255


def _is_blue(point) -> bool:
    return 100 <= point[0] <= 124 and \
           43 <= point[1] <= 255 and \
           46 <= point[2] <= 255


def _is_purple(point) -> bool:
    return 125 <= point[0] <= 155 and \
           43 <= point[1] <= 255 and \
           46 <= point[2] <= 255


__color_func = {
    "black": _is_black,
    "gray": _is_gray,
    "white": _is_white,
    "red": _is_red,
    "orange": _is_orange,
    "yellow": _is_yellow,
    "green": _is_green,
    "dblue": _is_deep_blue,
    "blue": _is_blue,
    "purple": _is_purple,
}


def _get_color(point) -> str:
    for color, func in __color_func.items():
        if func(point):
            return color
    return ""


def identify_color(img):
    # TODO: large image compute slow
    img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    color_count = defaultdict(int)
    point_count = 0
    for column_index in range(len(img)):
        row = img[column_index]
        for row_index in range(len(row)):
            point = img[column_index][row_index]
            c = _get_color(point)
            if not c:
                # print(column_index, row_index, point)
                continue
            color_count[_get_color(point)] += 1
            point_count += 1
    print(color_count)
    c = max(color_count.items(), key=operator.itemgetter(1))
    # logger.info(c, point_count)
    # return c[0]
    return color_count

# if __name__ == '__main__':
#     from tool_page import get_bar
#     import matplotlib.pyplot as plt
#
#     i = cv.imread("images/color1.png")
#     plt.imshow(cv.cvtColor(i, cv.COLOR_BGR2RGB))
#     height, width = i.shape[:2]
#     print(i, height, width)
#     plt.show()
#     identify_color(get_bar(i))
