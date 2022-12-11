from urllib.parse import unquote

import pyautogui
import pyperclip

from controller.gui_windows import back_origin_position
from utils.chrome_keyboard import refresh_page


def focus_page():
    # 放左边，点左边的右边
    pyautogui.click(1886, 419)


def continue_to_page():
    # 回到原来的页面
    focus_page()
    refresh_page()


def get_page_link() -> str:
    # 点击地址栏
    with back_origin_position():
        # 左屏幕
        pyautogui.click(614, 97)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')
    link = pyperclip.paste()
    link = unquote(link)
    return link
