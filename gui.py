import sys
import time
from collections import defaultdict
from datetime import datetime, timedelta
from typing import List
from PyQt5.QtCore import Qt, QDateTime
from PyQt5.QtWidgets import (QWidget, QPushButton, QDesktopWidget,
                             QHBoxLayout, QVBoxLayout, QApplication, QLineEdit, QLCDNumber, QLabel, QTimeEdit,
                             QMainWindow, QTabWidget,
                             QDialog, QBoxLayout)
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIntValidator
from utils.data_helper import store, get_data
from utils.time_helper import get_pass_time, get_remain_time, format_time


def make_one_line(widgets: List[QWidget], box: QBoxLayout) -> QBoxLayout:
    inbox = QHBoxLayout()
    for item in widgets:
        inbox.addWidget(item)
    box.addLayout(inbox)
    return inbox


def default_record():
    return [0, 0, 0, datetime(1, 1, 1)]


class TimeRecord(object):
    def __init__(self, day: int = 0, hour: int = 0, minute: int = 0):
        self.day = day
        self.hour = hour
        self.minute = minute
        self.t = datetime.now()
        self.empty = True

    def refresh(self):
        self.t = datetime.now()

    def set_by_key(self, key: str, d: int):
        print(f"set {key} {d}")
        setattr(self, key, d)
        self.refresh()
        self.empty = False

    @property
    def is_null(self):
        return self.empty

    def finished(self, now=datetime.now()):
        return not self.is_null and now > self.finish_time

    @property
    def finish_time(self) -> datetime:
        return self.t + timedelta(days=self.day, hours=self.hour, minutes=self.minute)

    @property
    def finish_time_str(self) -> str:
        return format_time(self.finish_time, "%Y-%m-%d %H:%M")

    def __str(self):
        return f"day={self.day} hour={self.hour} minute={self.minute} time={format_time(self.t)}"

    def __str__(self):
        return self.__str()

    def __repr__(self):
        return self.__str()


class ChongFan(QDialog):
    def __init__(self, parent=None):
        super(ChongFan, self).__init__(parent)
        self._db_name = "chongfandiguo.db"
        self._data = get_data(self._db_name)
        self._item = ("建造1", "建造2", "学院", "城堡", "募兵1", "募兵2", "治疗", "招募")
        if self._data is None:
            self._record = defaultdict(TimeRecord)
        else:
            self._record = self._data
        self._init_ui()

    def _init_ui(self):
        now = datetime.now()

        left_box = self._init_record_part(now)
        right_box = self._init_order_time_part(now)

        box2 = QHBoxLayout()
        box2.addLayout(left_box)
        box2.addStretch(1)
        box2.addLayout(right_box)
        self.setLayout(box2)

    def _update_by_key_attr(self, record_key, record_item_attr, context):
        self._record[record_key].set_by_key(record_item_attr, context)
        # TODO: 异步刷新
        print(self._record)
        store(self._record, self._db_name)
        return True

    def _init_record_part(self, now):
        """
        初始化左侧记录面板
        Args:
            now:

        Returns:

        """

        def update(record_key, record_item_attr):
            def _update(context):
                self._update_by_key_attr(record_key, record_item_attr, context)

            return _update

        box = QVBoxLayout()
        for item in self._item:
            day = QSpinBox(self)

            hour = QSpinBox(self)
            hour.setRange(0, 59)

            minute = QSpinBox(self)
            minute.setRange(0, 59)

            if item in self._record and not self._record[item].empty:
                # 再次判断以免直接初始化记录
                exist = self._record[item]
                remain_d, remain_h, remain_m = get_remain_time(exist.t, now, exist.day, exist.hour, exist.minute)
                day.setValue(remain_d)
                hour.setValue(remain_h)
                minute.setValue(remain_m)

            # 后关联，否则会触发更新
            day.valueChanged[int].connect(update(item, "day"))
            hour.valueChanged[int].connect(update(item, "hour"))
            minute.valueChanged[int].connect(update(item, "minute"))

            lb = QPushButton(f"{item}耗时：", self)
            lb.clicked.connect(lambda x: day.setValue(0) or hour.setValue(11) or minute.setValue(30))

            make_one_line([lb,
                           day, QLabel("天", self),
                           hour, QLabel("时", self),
                           minute, QLabel("分", self),
                           ], box)
        box.addStretch(1)
        return box

    def _init_order_time_part(self, now):
        box = QVBoxLayout()
        going = []
        finished = []
        for key, value in self._record.items():
            if value.is_null:
                continue
            if value.finished(now):
                finished.append(QLabel(f"{key} {value.finish_time_str} 结束", self))
            else:
                going.append(QLabel(f"{key} {value.finish_time_str} 结束", self))
        self.display_labels(box, finished, "已完成")
        self.display_labels(box, going, "进行中")
        box.addStretch(1)
        return box

    def display_labels(self, box, widgets, flag=""):
        if len(widgets) == 0:
            box.addWidget(QLabel(f"{flag}   无", self))
        else:
            box.addWidget(QLabel(f"{flag}{len(widgets)}项"))
            for item in widgets:
                box.addWidget(item)


class Pian(QDialog):
    def __init__(self, parent=None):
        super(Pian, self).__init__(parent)
        self.setStyleSheet("background-color: red")


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
