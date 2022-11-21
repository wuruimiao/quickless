import time

import pyautogui

"""
参考文档：
键盘鼠标文档：https://www.jianshu.com/p/e4f4ca3f6b52
chrome快捷键：https://support.google.com/chrome/answer/10483214?hl=zh-Hans
"""


def wait_page():
    time.sleep(2)


def close_page():
    pyautogui.hotkey('ctrl', 'w')


def back_page():
    pyautogui.hotkey('altleft', 'left')


def refresh_page():
    pyautogui.hotkey('ctrl', 'r')
    wait_page()


def pre_page():
    pyautogui.hotkey('ctrl', 'shiftleft', 'tab')


def next_page():
    pyautogui.hotkey('ctrl', 'tab')
