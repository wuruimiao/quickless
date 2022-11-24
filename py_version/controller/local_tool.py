import logging
import os
import hashlib

from db.connnection import db_session
from model.all import sync_table, FileFinger
from utils.time import get_now_str

logger = logging.getLogger(__name__)


def get_local_file_names(dir_name: str):
    for root, ds, fs in os.walk(dir_name):
        for f in fs:
            f_dir = os.path.join(root, f)
            yield f_dir


def get_file_finger(f_name: str):
    hash_md5 = hashlib.md5()
    with open(f_name, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def file_finger_exist(f_name: str) -> bool:
    return db_session.query(FileFinger.file_path)\
               .filter_by(file_path=f_name)\
               .first() is not None


def compute_file_finger():
    sync_table()
    dir_names = ("E:\BaiduNetdiskDownload",
                 "F:\BaiduNetdiskDownload",
                 "G:\BaiduNetdiskDownload",
                 "H:\BaiduNetdiskDownload")
    for driver in dir_names:
        for f_name in get_local_file_names(driver):
            if file_finger_exist(f_name):
                continue
            logger.info(f_name)
            finger = get_file_finger(f_name)
            created_at = updated_at = get_now_str()
            m = FileFinger(file_path=f_name, finger=finger, created_at=created_at, updated_at=updated_at)
            db_session.add(m)
            db_session.commit()
