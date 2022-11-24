from controller.local_tool import get_local_file_names, get_file_finger
from db.connnection import db_session
from model.all import FileFinger, sync_table
from utils.time import get_now_str


def main():
    sync_table()
    dir_names = ("E:\BaiduNetdiskDownload",
                 "F:\BaiduNetdiskDownload",
                 "G:\BaiduNetdiskDownload",
                 "H:\BaiduNetdiskDownload")
    for driver in dir_names:
        for f_name in get_local_file_names(driver):
            print(f_name)
            finger = get_file_finger(f_name)
            created_at = updated_at = get_now_str()
            m = FileFinger(file_path=f_name, finger=finger, created_at=created_at, updated_at=updated_at)
            db_session.add(m)
            db_session.commit()


if __name__ == '__main__':
    main()