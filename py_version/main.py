import sys
from view_gui.main import run_gui
from controller.local_file import compute_file_finger, del_empty_file, get_same_file
from controller.watch_keyboard import watch_keyboard

if __name__ == '__main__':
    command = sys.argv
    if len(command) == 1 or command[1] == "gui":
        run_gui()
        quit(0)

    command = command[1]
    if command == "file_finger":
        compute_file_finger()
    elif command == "empty_file":
        del_empty_file()
    elif command == "same_file":
        get_same_file()
    elif command == "watch":
        watch_keyboard()


