import pyautogui

from utils.chrome_keyboard import close_page, wait_page


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
