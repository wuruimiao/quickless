def get_bar(img):
    """
    下载工具页的进度页
    """
    return img[1420:1440, 73:1350, :]


def get_ensure_save_window(img):
    # 375 250     471 287
    return img[250:287, 375: 471, :]


def get_left_screen_page(img):
    # 7 170    1906 2088
    return img[170:2088, 7:1906, :]
