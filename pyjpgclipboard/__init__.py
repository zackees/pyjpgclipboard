"""
    Cross platform clipboard management.
"""

# pylint: disable=unused-import
# flake8: noqa

import sys

if sys.platform == "darwin":
    from .clipboard_darwin import clipboard_dump_jpg_darwin as clipboard_dump_jpg
    from .clipboard_darwin import clipboard_load_jpg_darwin as clipboard_load_jpg
elif sys.platform == "win32":
    from .clipboard_win32 import clipboard_dump_jpg_win32 as clipboard_dump_jpg
    from .clipboard_win32 import clipboard_load_jpg_win32 as clipboard_load_jpg
else:
    print(f"{__file__}: Unsupported platform: {sys.platform}, using stubbed versions.")

    def clipboard_dump_jpg(jpeg_path: str) -> None:
        """Copies the image at the given path into the system clipboard."""
        raise NotImplementedError(f"clipboard_dump_jpg not implemented for {sys.platform}")

    def clipboard_load_jpg(jpeg_path: str) -> None:
        """Copies the image at the given path into the system clipboard."""
        raise NotImplementedError(f"clipboard_load_jpg not implemented for {sys.platform}")
