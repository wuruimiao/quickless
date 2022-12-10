import pyautogui

from controller.gui_chrome import focus_page
from utils.chrome_keyboard import close_page, wait_page


def cancel_download_for_exist():
    pyautogui.typewrite(["enter"])
    pyautogui.click(1110, 856)
    close_page()


def download_from_tool_page():
    # 同时请求片段数框，改成3
    pyautogui.click(140, 998)
    pyautogui.typewrite(['backspace'])
    pyautogui.typewrite(['backspace'])
    pyautogui.typewrite("3")

    # 最大重试次数，改成15
    pyautogui.click(140, 1142)
    pyautogui.typewrite(['backspace'])
    pyautogui.typewrite("1")
    pyautogui.typewrite("5")

    # 选择保存目录
    pyautogui.click(158, 1389)
    wait_page()
    pyautogui.typewrite(['enter'])
    
    wait_page()
    # 下载，按钮位置可能变化，多点几次
    for y in range(1525, 1567, 6):
        pyautogui.click(1285, y)


def no_refresh_tool_download():
    focus_page()
    download_from_tool_page()


def finish_download():
    focus_page()
    close_page()
