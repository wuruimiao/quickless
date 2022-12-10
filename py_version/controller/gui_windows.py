from contextlib import contextmanager
import pyautogui


def back_left_screen():
    pyautogui.hotkey('winleft', 'ctrlleft', 'left')


@contextmanager
def back_origin_position():
    p = pyautogui.position()
    yield
    pyautogui.moveTo(p)
