import pyautogui

from utils.chrome_keyboard import refresh_page


def focus_page():
    # 放左边，点左边的右边
    pyautogui.click(1886, 419)


def continue_to_page():
    # 回到原来的页面
    focus_page()
    refresh_page()