from urllib.parse import unquote, urlparse

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


def new_page():
    pyautogui.hotkey('ctrl', 't')


def get_page_link() -> str:
    # 点击地址栏
    with back_origin_position():
        # 左屏幕
        pyautogui.click(614, 97)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.click(614, 97)
    link = pyperclip.paste()
    link = unquote(link)
    return link


def get_page_host() -> str:
    """
    获取页面的域名
    """
    link = get_page_link()
    link = urlparse(link)
    return link.netloc
