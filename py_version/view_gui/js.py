from PyQt5.QtWidgets import QDialog, QPushButton, QGridLayout

from controller.autogui_js import download_from_video_page
from controller.autogui_chrome import focus_page
from controller.autogui_thatwind_tool import cancel_download_for_exist, download_from_tool_page
from utils.chrome_keyboard import close_page, back_page, refresh_page, pre_page


class JS(QDialog):
    def __init__(self, parent=None):
        super(JS, self).__init__(parent)
        btn = QPushButton("视频页下载", self)
        btn.clicked.connect(download_from_video_page)
        btn1 = QPushButton("视频页下载并关闭视频页", self)
        btn1.clicked.connect(lambda x: download_from_video_page()
                                      or pre_page()
                                      or close_page())
        btn2 = QPushButton("下载完成", self)
        btn2.clicked.connect(lambda x: focus_page()
                                       or close_page()
                                       or back_page())
        btn3 = QPushButton("工具页下载", self)
        btn3.clicked.connect(lambda x: focus_page()
                                       or refresh_page()
                                       or download_from_tool_page())
        btn4 = QPushButton("取消下载", self)
        btn4.clicked.connect(cancel_download_for_exist)

        box = QGridLayout()
        box.addWidget(btn)
        box.addWidget(btn1)
        box.addWidget(btn2)
        box.addWidget(btn3)
        box.addWidget(btn4)
        self.setLayout(box)
