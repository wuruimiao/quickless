import pyautogui

from controller.gui_chrome import focus_page
from controller.gui_thatwind_tool import download_from_tool_page
from utils.chrome_keyboard import wait_page, refresh_page, close_page

"""
将页面放在屏幕右半边，下面的位置就是对的
TODO：使用相对位置
"""


def goto_tool_from_video_page():
    # 放右边
    # pyautogui.click(3697, 352)
    # 放左边
    pyautogui.click(1767, 352)


def download_from_video_page():
    goto_tool_from_video_page()
    wait_page()
    download_from_tool_page()


def no_refresh_tool_download():
    focus_page()
    download_from_tool_page()


def finish_download():
    focus_page()
    close_page()