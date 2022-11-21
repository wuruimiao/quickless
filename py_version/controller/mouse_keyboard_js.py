import pyautogui

from utils.chrome_keyboard import wait_page, close_page, refresh_page


"""
将页面放在屏幕右半边，下面的位置就是对的
TODO：使用相对位置
"""


def focus_page():
    pyautogui.click(3782, 788)


def goto_tool_from_video_page():
    pyautogui.click(3695, 340)


def cancel_download_for_exist():
    pyautogui.typewrite(["enter"])
    pyautogui.click(3001, 850)
    close_page()


def download_from_tool_page():
    # 同时请求片段数框
    pyautogui.click(2318, 990)
    # 同时请求片段数框，改成3
    pyautogui.click(2318, 990)
    pyautogui.typewrite(['backspace'])
    pyautogui.typewrite(['backspace'])
    pyautogui.typewrite("3")

    # 最大重试次数，改成15
    pyautogui.click(2333, 1139)
    pyautogui.typewrite(['backspace'])
    pyautogui.typewrite("1")
    pyautogui.typewrite("5")

    # 选择保存目录
    pyautogui.click(2098, 1365)
    wait_page()
    pyautogui.typewrite(['enter'])

    # 下载
    pyautogui.click(3178, 1509)


def download_from_video_page():
    focus_page()
    refresh_page()
    goto_tool_from_video_page()
    wait_page()
    download_from_tool_page()
