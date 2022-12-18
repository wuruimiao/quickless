import pyautogui

from controller.gui_thatwind_tool import DownloadPage
from utils.chrome_keyboard import Chrome

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
    Chrome.wait_page()
    DownloadPage.download_from_tool_page()
