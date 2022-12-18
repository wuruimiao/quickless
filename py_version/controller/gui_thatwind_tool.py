import time
from urllib.parse import urlparse, parse_qs

import pyautogui

from controller.gui_chrome import focus_page, get_page_link
from controller.gui_windows import back_origin_position
from utils.chrome_keyboard import Chrome
from utils.image import img_ocr, capture_screen


class _DownloadPage(object):
    def cancel_download_for_exist(self):
        with back_origin_position():
            pyautogui.typewrite(["enter"])
            pyautogui.click(1110, 856)
            Chrome.close_page()

    def download_from_tool_page(self):
        with back_origin_position():
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
            Chrome.wait_page()
            pyautogui.typewrite(['enter'])

            Chrome.wait_page()
            # 下载，按钮位置可能变化，多点几次
            for y in range(1525, 1567, 6):
                pyautogui.click(1285, y)

    def no_refresh_tool_download(self):
        with back_origin_position():
            focus_page()
            self.download_from_tool_page()

    def finish_download(self):
        with back_origin_position():
            focus_page()
            Chrome.close_page()

    def get_tool_page_origin_link(self) -> str:
        """
        获取工具页的原始下载页面
        """
        link = get_page_link()
        link = urlparse(link)

        params = parse_qs(link.params)
        params.update(parse_qs(link.query))
        params.update(parse_qs(link.fragment))
        link = params.get("referer", [])
        if len(link) > 0:
            link = link[0]
        return link

    def get_bar(self, img):
        """
        下载工具页的进度页
        """
        return img[1420:1440, 73:1350, :]

    def get_ensure_save_window(self, img):
        # 375 250     471 287
        return img[250:287, 375: 471, :]

    def get_link_part(self, img):
        # 30 454     1378 639
        return img[463:625, 51:1378, :]

    def need_refresh(self, download_page_img) -> bool:
        download_page_img = self.get_link_part(download_page_img)
        result = img_ocr(download_page_img)
        result = result.rstrip()
        return result in ("null", "")

    def ensure_ok(self):
        def ok(img) -> bool:
            if not self.need_refresh(img):
                return False
            Chrome.refresh_page()
        capture_screen(ok)


DownloadPage = _DownloadPage()
