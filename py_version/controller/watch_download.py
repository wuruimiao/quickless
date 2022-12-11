import logging
import time

import numpy as np
import cv2 as cv
from PIL import Image
from mss import mss
from utils.image import capture_screen
from controller.ai.identify import identify_color
from controller.img_page import get_bar, get_ensure_save_window
from controller.gui_thatwind_tool import cancel_download_for_exist, no_refresh_tool_download, finish_download

logger = logging.getLogger(__name__)

state = ""


def __watch_download(img):
    global state
    # display_img(img)
    color = identify_color(get_ensure_save_window(img))
    # TODO: 下载工具页未加载完成
    if len(color) > 3:
        # 需要取消下载
        state = "init"
        print("cancel download")
        cancel_download_for_exist()
    # display_img(get_ensure_save_window(img))

    color = identify_color(get_bar(img))
    if "blue" in color:
        pass
    elif "green" in color:
        # 下载完成，点击关闭
        finish_download()
        state = "finish"
    elif "white" in color and state != "ing":
        # 开始下载
        no_refresh_tool_download()
        state = "ing"
        pass
    elif state == "ing":
        # 判断是否是在下载中，不是看看是为啥不行

        pass
    time.sleep(2)


def watch_download():
    capture_screen(__watch_download)
