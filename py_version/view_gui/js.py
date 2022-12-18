import time

from PyQt5.QtWidgets import QDialog, QPushButton, QGridLayout

from controller.gui_chrome import focus_page
from controller.gui_js import download_from_video_page, goto_tool_from_video_page
from controller.gui_thatwind_tool import DownloadPage
from controller.gui_windows import back_left_screen, back_origin_position
from controller.gui_chrome import get_page_host
from utils.chrome_keyboard import Chrome
from utils.config import download_page, video_page
from utils.image import capture_screen


class JS(QDialog):
    def __init__(self, parent=None):
        super(JS, self).__init__(parent)

        def s():
            with back_origin_position():
                focus_page()
                for i in range(10):
                    goto_tool_from_video_page()
                    Chrome.wait_page(1)
                    DownloadPage.ensure_ok()
                    Chrome.pre_page()
                    if download_page != get_page_host():
                        Chrome.close_page()
                    Chrome.next_page()
                    time.sleep(1)

        btn = QPushButton("打开10个下载页", self)
        btn.clicked.connect(s)

        def s():
            with back_origin_position():
                focus_page()
                download_from_video_page()
                Chrome.pre_page()
                Chrome.close_page()

        btn1 = QPushButton("视频页无刷新下载并关闭视频页", self)
        btn1.clicked.connect(s)

        def s():
            with back_origin_position():
                focus_page()
                Chrome.next_page()
                download_from_video_page()
                Chrome.pre_page()
                Chrome.close_page()
                back_left_screen()

        btn7 = QPushButton("onetab页无刷新下载并关闭", self)
        btn7.clicked.connect(s)

        def s():
            with back_origin_position():
                download_from_video_page()
                Chrome.pre_page()
                Chrome.close_page()
                back_left_screen()

        btn2 = QPushButton("无刷新视频页下载并关闭", self)
        btn2.clicked.connect(s)

        btn3 = QPushButton("下载完成", self)
        btn3.clicked.connect(DownloadPage.finish_download)

        # btn4 = QPushButton("工具页下载", self)
        # btn4.clicked.connect(lambda x: focus_page()
        #                                or refresh_page()
        #                                or download_from_tool_page())

        def s():
            with back_origin_position():
                DownloadPage.no_refresh_tool_download()

        btn5 = QPushButton("无刷新工具页下载", self)
        btn5.clicked.connect(s)

        btn6 = QPushButton("取消下载", self)
        btn6.clicked.connect(DownloadPage.cancel_download_for_exist)

        box = QGridLayout()
        box.addWidget(btn)
        box.addWidget(btn5)
        box.addWidget(btn1)
        box.addWidget(btn7)
        box.addWidget(btn2)
        box.addWidget(btn3)
        # box.addWidget(btn4)
        box.addWidget(btn6)
        self.setLayout(box)
