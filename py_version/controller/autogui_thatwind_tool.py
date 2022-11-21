import pyautogui

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

    # 下载
    pyautogui.click(1294, 1573)
