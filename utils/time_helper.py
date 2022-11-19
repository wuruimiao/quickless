from datetime import datetime,timedelta
from typing import Tuple


def format_time(t: datetime, f: str = "%Y-%m-%d %H:%M:%S") -> str:
    return t.strftime(f)


def get_pass_time(early: datetime, latest: datetime) -> Tuple[int, int, int]:
    """
    获取已经过去了多少天、时、分
    Args:
        early:
        latest:

    Returns:

    """
    d = latest - early
    return d.days, d.seconds // 3600, (d.seconds // 60) % 60


def get_remain_time(early: datetime, latest: datetime, day: int, hour: int, minute:int) -> Tuple[int, int, int]:
    """

    Args:
        early: 记录生成的时间点
        latest: 最新的时间点
        day: 记录的天数
        hour: 记录的小时数
        minute: 记录的分钟数

    Returns: 距离记录的截止时间，还有多少天、时、分
    """
    deadline = early + timedelta(days=day, hours=hour, minutes=minute)
    if deadline <= latest:
        return 0, 0, 0
    return get_pass_time(latest, deadline)
