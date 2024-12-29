# Import built-in modules
from __future__ import annotations
from pathlib import Path
import os


def get_psd_files() -> dict[str, str]:
    files = {}
    this_root = Path(__file__).parent
    file_root = this_root / "files"
    for file_name in os.listdir(file_root):
        files[file_name] = str(file_root / file_name)
    return files
