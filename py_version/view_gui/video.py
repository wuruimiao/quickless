from PyQt5.QtWidgets import QDialog, QPushButton, QGridLayout
from utils.mouse_keyboard_js import refresh_page,\
    goto_tool_from_video_page, wait_page, download_from_tool_page, \
    cancel_download_for_exist, download_from_video_page, focus_page, \
    back_origin_page


class Pian(QDialog):
    def __init__(self, parent=None):
        super(Pian, self).__init__(parent)
        btn = QPushButton("视频页下载", self)
        btn.clicked.connect(download_from_video_page)
        btn1 = QPushButton("工具页下载", self)
        btn1.clicked.connect(lambda x: focus_page() or refresh_page() or download_from_tool_page())
        btn2 = QPushButton("取消下载", self)
        btn2.clicked.connect(cancel_download_for_exist)
        btn3 = QPushButton("视频页下载并返回", self)
        btn3.clicked.connect(lambda x: download_from_video_page() or back_origin_page())

        box = QGridLayout()
        box.addWidget(btn)
        box.addWidget(btn3)
        box.addWidget(btn1)
        box.addWidget(btn2)
        self.setLayout(box)
