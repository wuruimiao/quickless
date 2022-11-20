import time

import pyautogui
from pynput.keyboard import Controller, Key, Listener


# 监听按压
def on_press(key):
    try:
        print("正在按压:", format(key.char))
    except AttributeError:
        print("正在按压:", format(key))


def wait_page():
    time.sleep(0.5)


def refresh_page():
    pyautogui.hotkey('ctrl', 'r')
    wait_page()


def goto_tool_from_video_page():
    pyautogui.click(3695, 340)


def cancel_download_for_exist():
    pyautogui.typewrite(["enter"])
    pyautogui.click(3001, 850)


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


# 监听释放
def on_release(key):
    # print(format(key), type(key))
    if key == Key.page_up:
        # 从视频页下载
        print("按下了page up")
        refresh_page()
        goto_tool_from_video_page()
        wait_page()
        download_from_tool_page()
    elif key == Key.page_down:
        # 从工具页下载
        print("按下了page down")
        refresh_page()
        download_from_tool_page()
    elif key == Key.pause:
        print("按下了pause")
        cancel_download_for_exist()
    elif key == Key.esc:
        # 停止监听
        quit()


# 开始监听
def start_listen():
    # with Listener(on_press=on_press, on_release=on_release) as listener:
    with Listener(on_release=on_release) as listener:
        listener.join()


if __name__ == '__main__':
    """
    快捷键，操作网页视频下载
    """
    # 实例化键盘
    kb = Controller()
    print(pyautogui.size())
    print(pyautogui.position())
    # 开始监听,按esc退出监听
    start_listen()
