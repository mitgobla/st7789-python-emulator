import unittest
import st7789_emulator as st7789
from PIL import Image, ImageTk
import time

class TestST7789Emulator(unittest.TestCase):

    def setUp(self) -> None:
        self.image = Image.open("tests/240x240.png")
        self.emulator = st7789.ST7789(port=0, cs=1, dc=9, backlight=19)

    def test_image_present(self):
        time.sleep(1)
        self.emulator.display(self.image)
        assert self.emulator._gui._image != None
        time.sleep(1)

    def tearDown(self) -> None:
        if self.image:
            self.image.close()

        self.emulator._cleanup()