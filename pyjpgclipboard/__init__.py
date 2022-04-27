"""
    Cross platform clipboard management.
"""

# pylint: disable=unused-import
# flake8: noqa

import sys

if sys.platform == "darwin":
    from .clipboard_darwin import clipboard_dump_jpg_darwin as clipboard_dump_jpg
    from .clipboard_darwin import clipboard_load_jpg_darwin as clipboard_load_jpg
else:
    raise NotImplementedError(f"Unsupported platform: {sys.platform}")
