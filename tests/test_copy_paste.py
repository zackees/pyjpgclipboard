"""
    Tests the gab driver.
"""
import os
import sys
import tempfile
import unittest

from pyjpgclipboard import clipboard_dump_jpg, clipboard_load_jpg

HERE = os.path.dirname(os.path.abspath(__file__))
TEST_DATA = os.path.join(HERE, "data")
SMALL_IMG = os.path.join(TEST_DATA, "small.jpg")


class ClipBoardTester(unittest.TestCase):
    """Gab driver test framework."""

    def test_sanity(self) -> None:
        """Test that image assets are in their proper place"""
        self.assertTrue(os.path.exists(SMALL_IMG))

    def test_small_image_copy(self) -> None:
        """Tests that gab_post works"""
        clipboard_load_jpg(SMALL_IMG)
        # Create a temporary file in the system temp directory,
        # then test that the sizes are the same.
        with tempfile.NamedTemporaryFile(delete=False) as temp:
            temp.close()
            try:
                clipboard_dump_jpg(temp.name)
                # Windows, for some reason, stores the files slightly smaller.
                delta = 1 if sys.platform == "win32" else 0
                self.assertAlmostEqual(
                    os.path.getsize(temp.name),
                    os.path.getsize(SMALL_IMG),
                    delta=delta,
                    msg=f"{temp.name} is not the same size as {SMALL_IMG}",
                )
            finally:
                os.remove(temp.name)


if __name__ == "__main__":
    unittest.main()
