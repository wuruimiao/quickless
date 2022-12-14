import logging
import time

from controller.ai.identify import identify_color
from controller.gui_thatwind_tool import DownloadPage
from controller.gui_chrome import get_page_host
from utils.image import capture_screen

logger = logging.getLogger(__name__)

state = ""


def __watch_tool_page(img):
    global state
    # display_img(img)
    color = identify_color(DownloadPage.get_ensure_save_window(img))
    # TODO: 下载工具页未加载完成
    if len(color) > 3:
        # 需要取消下载
        state = "init"
        print("cancel download")
        DownloadPage.cancel_download_for_exist()
        return
    # display_img(get_ensure_save_window(img))

    color = identify_color(DownloadPage.get_bar(img))
    if "blue" in color:
        pass
    elif "green" in color:
        # 下载完成，点击关闭
        DownloadPage.finish_download()
        state = "finish"
    elif "white" in color and state != "ing":
        # 开始下载
        DownloadPage.no_refresh_tool_download()
        state = "ing"
        pass
    elif state == "ing":
        # 判断是否是在下载中，不是看看是为啥不行
        pass


def __watch_download(img):
    # host = get_page_host()
    # if host == "tools.thatwind.com":
    __watch_tool_page(img)
    # else:
    #     pass


def watch_download():
    capture_screen(__watch_download)
