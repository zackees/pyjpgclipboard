"""
    Win32 implementation of clipboard functions for copy paste jpg.
"""

# flake8: noqa
# pylint: disable=all

import win32clipboard  # type: ignore
import win32con  # type: ignore


def clipboard_load_jpg_win32(jpeg_path: str) -> None:
    """Copies the image at the given path into the system clipboard."""
    raise NotImplementedError("Not implemented on win32 yet")


def clipboard_dump_jpg_win32(jpeg_path: str) -> None:
    """Copies the image at the given path into the system clipboard."""
    raise NotImplementedError("Not implemented on win32 yet")
