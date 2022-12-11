from collections import defaultdict
from datetime import datetime

from PyQt5.QtWidgets import QDialog, QHBoxLayout, QSpinBox, QVBoxLayout, QPushButton, QLabel

from model.time_record import TimeRecord
from utils.data import get_data, store
from utils.gui import make_one_line, highlight
from utils.time import get_remain_time


class ChongFan(QDialog):
    def __init__(self, parent=None):
        super(ChongFan, self).__init__(parent)
        self._item = ("建造1", "建造2", "学院", "城堡", "募兵1", "募兵2", "治疗", "免费招募")

        self._db_name = "chongfandiguo.db"
        d = get_data(self._db_name)
        if d is None:
            self._record = defaultdict(TimeRecord)
        else:
            self._record = d

        self._init_ui()

    def _init_ui(self):
        now = datetime.now()

        left_box = self._init_record_part(now)
        right_box = self._init_ordered_time_part(now)

        box = QHBoxLayout()
        box.addLayout(left_box)
        box.addStretch(1)
        box.addLayout(right_box)
        self.setLayout(box)

    def _update_by_key_attr(self, record_key, record_item_attr, context):
        self._record[record_key].set_by_key(record_item_attr, context)
        # TODO: 异步刷新
        print(self._record)
        store(self._record, self._db_name)
        return True

    def init_time_box(self, item, day: QSpinBox, hour: QSpinBox, minute: QSpinBox, second: QSpinBox):
        def _init():
            now = datetime.now()
            self._record[item].day = 0
            self._record[item].hour = 11
            self._record[item].minute = 30
            self._record[item].second = 0
            self._record[item].t = now
            self.update_time_box_by_record(now, item, day, hour, minute, second)

        return _init

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
            day, hour, minute, second = self._init_time_input()
            if item in self._record and not self._record[item].empty:
                # 再次判断以免直接初始化记录
                self.update_time_box_by_record(now, item, day, hour, minute, second)

            self.connect_time_box_action(day, hour, item, minute, second, update)

            btn = QPushButton(f"{item}耗时", self)
            btn.clicked.connect(self.init_time_box(item, day, hour, minute, second))

            make_one_line([btn,
                           day, QLabel("天", self),
                           hour, QLabel("时", self),
                           minute, QLabel("分", self),
                           second, QLabel("秒", self),
                           ], box)
        box.addStretch(1)
        return box

    def connect_time_box_action(self, day, hour, item, minute, second, update):
        # 后关联，否则会触发更新
        day.valueChanged[int].connect(update(item, "day"))
        hour.valueChanged[int].connect(update(item, "hour"))
        minute.valueChanged[int].connect(update(item, "minute"))
        second.valueChanged[int].connect(update(item, "second"))

    def update_time_box_by_record(self, now, item, day, hour, minute, second):
        exist = self._record[item]
        remain_d, remain_h, remain_m, remain_s = get_remain_time(
            exist.t, now, exist.day, exist.hour, exist.minute, exist.second)
        day.setValue(remain_d)
        hour.setValue(remain_h)
        minute.setValue(remain_m)
        second.setValue(remain_s)

    def _init_time_input(self):
        day = QSpinBox(self)
        hour = QSpinBox(self)
        hour.setRange(0, 59)
        minute = QSpinBox(self)
        minute.setRange(0, 59)
        second = QSpinBox(self)
        second.setRange(0, 59)
        return day, hour, minute, second

    def _init_ordered_time_part(self, now):
        """
        初始化右边，根据时间排序的事件
        Args:
            now:

        Returns:

        """
        box = QVBoxLayout()
        going = []
        finished = []

        for key, value in self._record.items():
            if value.is_null:
                continue
            _item = (key, value.finish_time_str)
            if value.finished(now):
                finished.append(_item)
            else:
                going.append(_item)
        finished.sort(key=lambda x: x[1])
        going.sort(key=lambda x: x[1])

        self.display_labels(box, [QLabel(f"{item[1]}{item[0]}已完成", self) for item in finished], "已完成")
        box.addWidget(QLabel("\n", self))

        t = [QLabel(f"{item[1]}{item[0]}将完成", self) for item in going]
        if len(t) > 0:
            t[0] = highlight(t[0])
        self.display_labels(box, t, "进行中")
        box.addWidget(QLabel("\n", self))
        box.addStretch(1)
        return box

    def display_labels(self, box, widgets, flag=""):
        if len(widgets) == 0:
            box.addWidget(QLabel(f"{flag}   无", self))
        else:
            box.addWidget(QLabel(f"{flag}{len(widgets)}项"))
            for item in widgets:
                box.addWidget(item)
