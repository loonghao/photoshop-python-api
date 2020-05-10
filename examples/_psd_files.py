import os


def get_psd_files():
    files = {}
    this_root = os.path.dirname(__file__)
    file_root = os.path.join(this_root, "files")
    for file_name in os.listdir(file_root):
        files[file_name] = os.path.join(file_root, file_name)
    return files
