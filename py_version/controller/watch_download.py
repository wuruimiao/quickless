import logging
import time

import numpy as np
import cv2 as cv
from PIL import Image
from mss import mss

from controller.ai.identify import identify_color
from controller.ai.tool_page import get_bar, get_ensure_save_window
from utils.image import display_img, display_img_by_name
from controller.gui_thatwind_tool import cancel_download_for_exist, no_refresh_tool_download, finish_download
from controller.gui_windows import back_origin_position
logger = logging.getLogger(__name__)


def watch_download():
    # display_img_by_name("images/color1.png")
    mon = {'left': 0, 'top': 0, 'width': 3804, 'height': 2160}
    count = 0
    state = ""
    with mss() as sct:
        while True:
            cap = sct.grab(mon)
            img = Image.frombytes('RGB', (cap.width, cap.height), cap.rgb, )
            img = np.array(img)
            img = cv.cvtColor(img, cv.COLOR_RGB2BGR)
            # display_img(img)
            color = identify_color(get_ensure_save_window(img))
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
                state = "init"
            elif "white" in color and state != "ing":
                # 开始下载
                no_refresh_tool_download()
                state = "ing"
                pass

            time.sleep(2)
