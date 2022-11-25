import logging
import os
import hashlib
import shutil

from sqlalchemy.orm import aliased
from sqlalchemy import and_
from db.connnection import db_session
from model.all import sync_table, FileFinger
from utils.time import get_now_str

logger = logging.getLogger(__name__)

dir_names = ("E:\BaiduNetdiskDownload",
             "F:\BaiduNetdiskDownload",
             "G:\BaiduNetdiskDownload",
             "H:\BaiduNetdiskDownload")


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
    return db_session.query(FileFinger.file_path) \
               .filter_by(file_path=f_name) \
               .first() is not None


def compute_file_finger():
    sync_table()
    for driver in dir_names:
        for f_name in get_local_file_names(driver):
            if file_finger_exist(f_name):
                logger.info(f"{f_name} exist")
                continue
            logger.info(f"{f_name} will compute")
            finger = get_file_finger(f_name)
            created_at = updated_at = get_now_str()
            m = FileFinger(file_path=f_name, finger=finger, created_at=created_at, updated_at=updated_at)
            db_session.add(m)
            db_session.commit()


def get_same_file():
    f1 = aliased(FileFinger, name="f1")
    f2 = aliased(FileFinger, name="f2")
    files = db_session.query(f1.file_path, f2.file_path) \
        .join(f2, and_(f1.finger == f2.finger, f1.file_path != f2.file_path)) \
        .all()
    for f in files:
        logger.info(f"\n{f[0]} \n {f[1]} \n is same========")


def del_file(file_path: str):
    os.remove(file_path)
    db_session.delete(FileFinger).filter_by(file_path=file_path).delete()


def rename_file(file_path: str, new_file_name: str):
    pass


def del_empty_file():
    for driver in dir_names:
        for f_path in get_local_file_names(driver):
            if os.path.getsize(f_path):
                continue
            f_paths = os.path.split(f_path)
            if "downloading" in f_paths[-1] or "baiduyun" in f_paths[-1]:
                # logger.info(f"{f_path} is baidu, will not del")
                continue
            logger.info(f"{f_path} will be removed")
            db_session.query(FileFinger).filter_by(file_path=f_path).delete()
            new_f_path = f"D:\\code{f_path[2:]}"
            logger.info(f"{new_f_path}")
            os.makedirs(new_f_path)
            shutil.move(f_path, new_f_path)
