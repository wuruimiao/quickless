import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QDesktopWidget, QTabWidget, QApplication)

from view.chong_fan import ChongFan
from view.video import Pian


class Example(QTabWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('效率')
        # 大小位置
        # self.setGeometry(300, 300, 300, 220)
        self.resize(800, 800)
        self.center()
        # self.statusBar().showMessage('Ready')
        self.chong_fan = ChongFan()
        self.pian = Pian()
        self.addTab(self.chong_fan, "重返帝国")
        self.addTab(self.pian, "视频")
        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
            self.close()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
