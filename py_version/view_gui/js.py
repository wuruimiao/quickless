from PyQt5.QtWidgets import QDialog, QPushButton, QGridLayout

from controller.autogui_js import download_from_video_page, goto_tool_from_video_page
from controller.autogui_chrome import focus_page, continue_to_page
from controller.autogui_thatwind_tool import cancel_download_for_exist, download_from_tool_page
from controller.autogui_windows import back_left_screen
from utils.chrome_keyboard import close_page, back_page, refresh_page, pre_page, wait_page, next_page


class JS(QDialog):
    def __init__(self, parent=None):
        super(JS, self).__init__(parent)
        # btn = QPushButton("视频页下载", self)
        # btn.clicked.connect(lambda x: continue_to_page()
        #                               or download_from_video_page()
        #                               or back_left_screen())
        # btn1 = QPushButton("视频页下载并关闭视频页", self)
        # btn1.clicked.connect(lambda x: continue_to_page()
        #                                or download_from_video_page()
        #                                or pre_page()
        #                                or close_page()
        #                                or back_left_screen())
        btn7 = QPushButton("onetab页无刷新下载并关闭", self)
        btn7.clicked.connect(lambda x: next_page()
                                       or download_from_video_page()
                                       or pre_page()
                                       or close_page()
                                       or back_left_screen())
        btn2 = QPushButton("无刷新视频页下载并关闭", self)
        btn2.clicked.connect(lambda x: download_from_video_page()
                                       or pre_page()
                                       or close_page()
                                       or back_left_screen())
        btn3 = QPushButton("下载完成", self)
        btn3.clicked.connect(lambda x: focus_page()
                                       or close_page()
                                       or back_page())
        # btn4 = QPushButton("工具页下载", self)
        # btn4.clicked.connect(lambda x: focus_page()
        #                                or refresh_page()
        #                                or download_from_tool_page())
        btn5 = QPushButton("无刷新工具页下载", self)
        btn5.clicked.connect(lambda x: focus_page()
                                       or download_from_tool_page())
        btn6 = QPushButton("取消下载", self)
        btn6.clicked.connect(cancel_download_for_exist)

        box = QGridLayout()
        # box.addWidget(btn)
        # box.addWidget(btn1)
        box.addWidget(btn2)
        box.addWidget(btn3)
        # box.addWidget(btn4)
        box.addWidget(btn5)
        box.addWidget(btn6)
        self.setLayout(box)
