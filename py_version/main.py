import logging
import sys
from view_gui.main import run_gui
from controller.local_file import compute_file_finger, del_empty_file, get_same_file, del_same_file, compute_dir_file_finger
from controller.watch_keyboard import watch_keyboard

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    argv = sys.argv
    if len(argv) == 1 or argv[1] == "gui":
        run_gui()
        quit(0)

    command = argv[1]
    if command == "file_finger":
        compute_file_finger()
    elif command == "empty_file":
        del_empty_file()
    elif command == "same_file":
        get_same_file()
    elif command == "watch":
        watch_keyboard()
    elif command == "del_same":
        del_same_file()
    elif command == "compute_dir":
        if len(argv) <= 2:
            logger.info(f"please spec dir")
        else:
            compute_dir_file_finger(argv[2])


