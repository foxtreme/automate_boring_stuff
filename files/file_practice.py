import os

dir_files = os.listdir()


def human_size(size, units=(' bytes', ' KB', ' MB', ' GB', ' TB', ' PB', ' EB')):
    """
    Returns a human readable string representation of bytes
    """
    return "{}".rjust(6 - len(str(size))).format(str(size)) + units[0] if size < 1024 else human_size(size >> 10, units[1:])


def prettify_list_dir():
    """
    Lists files and dirs in current dir
    in the following format <filename> --- <size> || <'Folder'>
    """
    print(" Files in '{}' directory ".center(50, "-").format(os.path.basename(os.getcwd())))
    dir_files.sort()
    for file in dir_files:
        filename = "- {}".ljust(30 - len(file), " ").format(file)
        if os.path.isfile(file) and not file.startswith((".", "__")):
            size = human_size(os.path.getsize(file))
            print("{} {}".format(
                filename,
                size
            ))
        elif os.path.isdir(file) and not file.startswith((".", "__")):
            print("{} {}".format(
                filename,
                "Folder".rjust(11, " ")
            ))


prettify_list_dir()
