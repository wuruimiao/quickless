# 监听按压
import pyautogui
from pynput.keyboard import Key, Listener, Controller

from controller.gui_js import goto_tool_from_video_page
from controller.gui_thatwind_tool import DownloadPage
# cancel_download_for_exist, download_from_tool_page
from utils.chrome_keyboard import Chrome
# wait_page, refresh_page


def on_press(key):
    try:
        print("正在按压:", format(key.char))
    except AttributeError:
        print("正在按压:", format(key))


# 监听释放
def on_release(key):
    # print(format(key), type(key))
    if key == Key.page_up:
        # 从视频页下载
        print("按下了page up")
        Chrome.refresh_page()
        goto_tool_from_video_page()
        Chrome.wait_page()
        DownloadPage.download_from_tool_page()
    elif key == Key.page_down:
        # 从工具页下载
        print("按下了page down")
        Chrome.refresh_page()
        DownloadPage.download_from_tool_page()
    elif key == Key.pause:
        print("按下了pause")
        DownloadPage.cancel_download_for_exist()
    elif key == Key.delete:
        # 停止监听
        quit()


# 开始监听
def start_listen():
    # with Listener(on_press=on_press, on_release=on_release) as listener:
    with Listener(on_release=on_release) as listener:
        listener.join()


def watch_keyboard():
    """
    快捷键，操作网页视频下载
    """
    # 实例化键盘
    kb = Controller()
    print(pyautogui.size())
    print(pyautogui.position())
    # 开始监听,按esc退出监听
    start_listen()
