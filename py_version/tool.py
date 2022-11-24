from utils.log import init_log
from controller.local_tool import compute_file_finger

if __name__ == '__main__':
    init_log("tool.log")
    compute_file_finger()
