def get_bar(img):
    """
    下载工具页的进度页
    """
    return img[1420:1440, 73:1350, :]


def get_ensure_save_window(img):
    # 373 166     1152 693
    return img[166:693, 373: 1152, :]