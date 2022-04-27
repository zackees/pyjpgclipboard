"""
    Win32 implementation of clipboard functions for copy paste jpg.
"""

# flake8: noqa
# pylint: disable=all

import win32clipboard  # type: ignore
import win32con  # type: ignore


def clipboard_load_jpg_win32(jpeg_path: str) -> None:
    """Copies the image at the given path into the system clipboard."""
    # Load jpeg image into byte array
    with open(jpeg_path, "rb") as f:
        jpeg_bytes = f.read()
    # Send jpeg bytes to system clipboard.
    win32clipboard.OpenClipboard()
    try:
        # Set clipboard data to jpeg image
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32con.CF_DIB, jpeg_bytes)
    finally:
        win32clipboard.CloseClipboard()


def clipboard_dump_jpg_win32(jpeg_path: str) -> None:
    """Copies the image at the given path into the system clipboard."""
    # Get jpeg bytes from system clipboard.
    win32clipboard.OpenClipboard()
    try:
        jpeg_bytes = win32clipboard.GetClipboardData(win32con.CF_DIB)
    finally:
        win32clipboard.CloseClipboard()
    # Write jpeg bytes to file.
    with open(jpeg_path, mode="wb") as f:
        f.write(jpeg_bytes)
