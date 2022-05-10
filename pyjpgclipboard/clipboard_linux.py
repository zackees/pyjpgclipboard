"""
    Linux implementation of clipboard functions fotor copy paste jpg.
"""


import os
import subprocess

DISPLAY = os.environ.get("DISPLAY", ":0")


def clipboard_load_jpg_linux(jpeg_path: str) -> None:
    """Copies the image at the given path into the system clipboard."""
    cmd = f'xclip -d {DISPLAY} -selection clipboard -t image/jpeg -i "{jpeg_path}"'
    subprocess.run(cmd, shell=True, check=False)


def clipboard_dump_jpg_linux(jpeg_path: str) -> None:
    """Dumps the image contents into the currnet path."""
    cmd = f'xclip -d {DISPLAY} -selection clipboard -t image/jpeg -o > "{jpeg_path}"'
    subprocess.run(cmd, shell=True, check=False)
