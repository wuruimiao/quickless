import logging
import sys


logger = logging.getLogger(__name__)

if __name__ == '__main__':
    argv = sys.argv
    if len(argv) == 1 or argv[1] == "gui":
        from view_gui.main import run_gui
        run_gui()
        quit(0)

    command = argv[1]
    if command == "file_finger":
        from controller.local_file import compute_file_finger
        compute_file_finger()
    elif command == "empty_file":
        from controller.local_file import del_empty_file
        del_empty_file()
    elif command == "same_file":
        from controller.local_file import get_same_file
        get_same_file()
    elif command == "watch":
        from controller.watch_keyboard import watch_keyboard
        watch_keyboard()
    elif command == "del_same":
        from controller.local_file import del_same_file
        del_same_file()
    elif command == "compute_dir":
        if len(argv) <= 2:
            logger.info(f"please spec dir")
        else:
            from controller.local_file import compute_dir_file_finger
            compute_dir_file_finger(argv[2])
    elif command == "renew_dir":
        if len(argv) <= 2:
            logger.info(f"please spec dir")
        else:
            from controller.local_file import renew_dir_files
            renew_dir_files(argv[2])
    elif command == "watch_download":
        from controller.watch_download import watch_download
        watch_download()
