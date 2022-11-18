from datetime import datetime
from typing import Tuple


def get_pass_time(early: datetime, latest: datetime) -> Tuple[int, int, int]:
    """

    Args:
        early:
        latest:

    Returns:

    """
    d = latest - early
    return d.days, d.seconds // 3600, (d.seconds // 60) % 60
