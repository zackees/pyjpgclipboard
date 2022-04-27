"""
    Cross platform clipboard management.
"""

# pylint: disable=unused-import
# flake8: noqa

import sys


if sys.platform == "darwin":
    from .clipboard_darwin import clipboard_store_jpg_darwin as clipboard_store_jpg
    from .clipboard_darwin import clipboard_get_jpg_darwin as clipboard_get_jpg
else:
    raise NotImplementedError(f"Unsupported platform: {sys.platform}")
