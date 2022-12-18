from contextlib import contextmanager

import pyautogui


def back_left_screen():
    pyautogui.hotkey('winleft', 'ctrlleft', 'left')


@contextmanager
def back_origin_position():
    p = pyautogui.position()
    yield
    pyautogui.moveTo(p)


def get_left_screen_page(img):
    # 7 170    1906 2088
    return img[170:2088, 7:1906, :]
