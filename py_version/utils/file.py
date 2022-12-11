import os


def cmp_file(f1: str, f2: str) -> bool:
    st1 = os.stat(f1)
    st2 = os.stat(f2)

    # 比较文件大小
    if st1.st_size != st2.st_size:
        return False

    size = 8 * 1024
    with open(f1, 'rb') as fp1, open(f2, 'rb') as fp2:
        while True:
            b1 = fp1.read(size)  # 读取指定大小的数据进行比较
            b2 = fp2.read(size)
            if b1 != b2:
                return False
            if not b1:
                return True
