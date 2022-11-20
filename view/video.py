from PyQt5.QtWidgets import QDialog


class Pian(QDialog):
    def __init__(self, parent=None):
        super(Pian, self).__init__(parent)
        self.setStyleSheet("background-color: red")
