from PyQt5.QtWidgets import QDialog, QPushButton, QGridLayout

from utils.mouse_keyboard_js import refresh_page, \
    download_from_tool_page, \
    cancel_download_for_exist, download_from_video_page, focus_page, \
    back_page, close_page


class Pian(QDialog):
    def __init__(self, parent=None):
        super(Pian, self).__init__(parent)
        btn = QPushButton("视频页下载", self)
        btn.clicked.connect(download_from_video_page)
        btn4 = QPushButton("下载完成", self)
        btn4.clicked.connect(lambda x: focus_page() or close_page() or back_page())
        btn1 = QPushButton("工具页下载", self)
        btn1.clicked.connect(lambda x: focus_page() or refresh_page() or download_from_tool_page())
        btn2 = QPushButton("取消下载", self)
        btn2.clicked.connect(cancel_download_for_exist)

        box = QGridLayout()
        box.addWidget(btn)
        box.addWidget(btn4)
        box.addWidget(btn1)
        box.addWidget(btn2)
        self.setLayout(box)
