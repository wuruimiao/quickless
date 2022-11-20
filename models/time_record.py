from datetime import datetime, timedelta

from utils.time_helper import format_time


class TimeRecord(object):
    def __init__(self, day: int = 0, hour: int = 0, minute: int = 0, second: int = 0):
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
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
        return f"day={self.day} hour={self.hour} minute={self.minute} second={self.second} time={format_time(self.t)}"

    def __str__(self):
        return self.__str()

    def __repr__(self):
        return self.__str()
