import time

import pyautogui
from pynput.keyboard import Controller, Key, Listener


# 参考文档：https://www.jianshu.com/p/e4f4ca3f6b52


def wait_page():
    time.sleep(1)


def refresh_page():
    pyautogui.hotkey('ctrl', 'r')
    wait_page()


def focus_page():
    pyautogui.click(1946, 787)


def goto_tool_from_video_page():
    pyautogui.click(3695, 340)


def cancel_download_for_exist():
    pyautogui.typewrite(["enter"])
    pyautogui.click(3001, 850)
    pyautogui.hotkey('ctrl', 'w')


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
    pyautogui.click(3142, 1515)


def back_origin_page():
    # 上一个页面，返回前一页
    pyautogui.hotkey('shiftleft', 'j')
    pyautogui.click(1957, 99)


def download_from_video_page():
    focus_page()
    refresh_page()
    goto_tool_from_video_page()
    wait_page()
    download_from_tool_page()
