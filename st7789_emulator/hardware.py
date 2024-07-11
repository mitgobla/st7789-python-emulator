from PIL import Image
import threading
import atexit

from .gui import ST7789Gui

class ST7789(object):

    _idnext: int = 0

    def __init__(
            self,
            port: int,
            cs: int,
            dc: int,
            backlight: int | None = None,
            rst: int | None = None,
            width: int = 240,
            height: int = 240,
            rotation: int = 90,
            invert: bool = True,
            spi_speed_hz: int = 4000000,
            offset_left: int = 0,
            offset_top: int = 0
    ):

        self._id = self._idnext
        self._idnext += 1

        if rotation not in [0, 90, 180, 270]:
            raise ValueError(f"Invalid rotation {rotation}")

        if width != height and rotation in [90, 270]:
            raise ValueError(
                f"Invalid rotation {rotation} for {width}x{height} resolution"
            )

        self._spi = (port, cs, spi_speed_hz)
        self._dc = dc
        self._bl = backlight
        self._rst = rst
        self._width = width
        self._height = height
        self._rotation = rotation
        self._invert = invert

        self._offset_left = offset_left
        self._offset_top = offset_top

        # GUI setup
        self._gui = ST7789Gui(self._id)
        self._gui_thread = threading.Thread(target=self._gui.run)
        self._gui_thread.start()
        self._gui.update_image(Image.new('RGB', (self.width, self.height)))
        atexit.register(self._cleanup)

    def __del__(self):
        self._cleanup()

    def _cleanup(self):
        if self._gui:
            self._gui.stop()

        if self._gui_thread:
            self._gui_thread.join()

    def set_pin(self, pin, state):
        pass

    def send(self, data, is_data=True, chunk_size=4096):
        pass

    def set_backlight(self, value):
        pass

    @property
    def width(self):
        return (
            self._width
            if self._rotation == 0 or self._rotation == 180
            else self._height
        )

    @property
    def height(self):
        return (
            self._height
            if self._rotation == 0 or self._rotation == 180
            else self._width
        )

    def command(self, data):
        pass

    def reset(self):
        pass

    def _init(self):
        pass

    def begin(self):
        pass

    def set_window(self, x0=0, y0=0, x1=None, y1=None):
        pass

    def display(self, image: Image.Image):
        image.rotate(self._rotation)
        image.resize((self.width, self.height), Image.Resampling.NEAREST)
        self._gui.update_image(image)

    def image_to_data(self, image: Image.Image, rotation: int = 0):
        pass