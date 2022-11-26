import logging
from multiprocessing import Pool
from multiprocessing.pool import ThreadPool
import os
import hashlib
import shutil

from sqlalchemy.orm import aliased
from sqlalchemy import and_
from db.connnection import db_session
from model.all import sync_table, FileFinger
from utils.time import get_now_str

logger = logging.getLogger(__name__)

dir_names = (
    "G:\\BaiduNetdiskDownload",
    "E:\\BaiduNetdiskDownload",
    "F:\\BaiduNetdiskDownload",
    "H:\\BaiduNetdiskDownload"
)


def is_baiduyun_tmp(f_path):
    return "baiduyun" in f_path or "downloading" in f_path


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


def compute_dir_file_finger(_dir: str):
    logger.info(f"will compute dir {_dir}")
    for f_name in get_local_file_names(_dir):
        if file_finger_exist(f_name):
            logger.info(f"{f_name} exist")
            continue
        logger.info(f"{f_name} will compute")
        finger = get_file_finger(f_name)
        created_at = updated_at = get_now_str()
        m = FileFinger(file_path=f_name, finger=finger, created_at=created_at, updated_at=updated_at)
        db_session.add(m)
        db_session.commit()


def compute_file_finger():
    # pool = ThreadPool(processes=5)
    pool = Pool(processes=4)
    sync_table()
    res = []
    for driver in dir_names:
        r = pool.apply_async(compute_dir_file_finger, (driver,))
        res.append(r)
    for r in res:
        r.get()
    pool.close()
    pool.join()


def get_same_file():
    f1 = aliased(FileFinger, name="f1")
    f2 = aliased(FileFinger, name="f2")
    files = db_session.query(f1.file_path, f2.file_path) \
        .join(f2, and_(f1.finger == f2.finger, f1.file_path != f2.file_path)) \
        .all()
    return files


def del_same_file():
    files = get_same_file()
    for f1, f2 in files:
        if is_baiduyun_tmp(f1) or is_baiduyun_tmp(f2):
            continue
        need_del = True
        if not os.path.exists(f1):
            # f1不存在，直接删除
            del_file(f1)
            need_del = False
        if not os.path.exists(f2):
            del_file(f2)
            need_del = False
            continue

        if not need_del:
            continue
        del_f = max([f1, f2], key=len)
        logger.info(f"\n{f1}\n{f2}\n is same========")
        logger.info(f"will del\n{del_f}")
        del_file(del_f)


def del_file(f_path: str):
    db_session.query(FileFinger).filter_by(file_path=f_path).delete()
    if os.path.exists(f_path):
        os.remove(f_path)
        # new_f_path = f"D:\\code{f_path[2:]}"
        # f_base_path = os.path.split(new_f_path)[0]
        # if not os.path.exists(f_base_path):
        #     # 新目录不存在，新建
        #     os.makedirs(os.path.split(new_f_path)[0])
        # if os.path.exists(new_f_path):
        #     # 新目录已存在，直接删除
        #     if os.path.exists(f_path):
        #         shutil.rmtree(f_path)
        # else:
        #     shutil.move(f_path, new_f_path)
    db_session.commit()


def del_empty_file():
    for driver in dir_names:
        for f_path in get_local_file_names(driver):
            if os.path.getsize(f_path):
                continue
            if is_baiduyun_tmp(f_path):
                # logger.info(f"{f_path} is baidu, will not del")
                continue
            logger.info(f"{f_path} will be removed")
            del_file(f_path)


def rename_path():
    # 重命名文件夹时，也要更新数据库，不然数据会不准
    pass