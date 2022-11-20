# # -*- coding: utf-8 -*-
#
# import sys
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import Qt
#
#
# class Example(QWidget):
#
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#         hbox = QHBoxLayout(self)
#
#         topleft = QFrame(self)
#         topleft.setFrameShape(QFrame.StyledPanel)
#         # 我们使用了一个样式框架，为了让框架组件之间的分割线看的明显。我们使用了一个样式框架，为了让框架组件之间的分割线看的明显。
#
#         topright = QFrame(self)
#         topright.setFrameShape(QFrame.StyledPanel)
#
#         bottom = QFrame(self)
#         bottom.setFrameShape(QFrame.StyledPanel)
#
#         splitter1 = QSplitter(Qt.Horizontal)
#         splitter1.addWidget(topleft)
#         splitter1.addWidget(topright)
#         # 我们创建了一个分割框组件并且在这个分割框中添加进入两个框架组件。
#
#         splitter2 = QSplitter(Qt.Vertical)
#         splitter2.addWidget(splitter1)
#         splitter2.addWidget(bottom)
#         # 我们把第一个分割框添加进另一个分割框组件中。
#
#         hbox.addWidget(splitter2)
#         self.setLayout(hbox)
#
#         self.setGeometry(300, 300, 300, 200)
#         self.setWindowTitle('QSplitter')
#         self.show()
#
#     def onChanged(self, text):
#         self.lbl.setText(text)
#         self.lbl.adjustSize()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())


import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
# from PyQt5.QtWebEngine import QtWebEngine

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('百度')  #窗口标题
        self.setGeometry(5,30,1355,730)  #窗口的大小和位置设置
        self.browser=QWebEngineView()
        #加载外部的web界面
        self.browser.load(QUrl('https://gamer.qq.com/v2/cloudgame/game/95818?ichannel=pcgames0Fpcgames1'))
        self.setCentralWidget(self.browser)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=MainWindow()
    win.show()
    app.exit(app.exec_())