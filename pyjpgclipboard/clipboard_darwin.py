"""
    MacOS implementation of clipboard functions for copy paste jpg.
"""


import subprocess


def clipboard_store_jpg_darwin(jpeg_path: str) -> None:
    """Copies the image at the given path into the system clipboard."""
    subprocess.run(
        [
            "osascript",
            "-e",
            f'set the clipboard to (read (POSIX file "{jpeg_path}") as JPEG picture)',
        ],
        check=True,
    )


def clipboard_get_jpg_darwin(jpeg_path: str) -> None:
    """Copies the image at the given path into the system clipboard."""
    commands = [
        "osascript",
        "-e set pastedImage to "
        f'(open for access POSIX file "{jpeg_path}" with write permission)',
        "-e try",
        "-e     write (the clipboard as JPEG picture) to pastedImage",
        "-e end try",
        "-e close access pastedImage",
    ]
    # commands = get_osascript_args(commands)
    subprocess.run(
        commands,
        check=True,
    )
