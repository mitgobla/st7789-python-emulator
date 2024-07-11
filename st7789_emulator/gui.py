import tkinter as tk
from PIL import Image, ImageTk
import threading
import queue

class ST7789Gui(object):

    def __init__(self, id: int):
        self._id = id
        self._root: tk.Tk | None = None
        self._image_label: tk.Label | None = None
        self._image: ImageTk.PhotoImage | None = None

        self._update_queue = queue.Queue()
        self._stop_flag = threading.Event()

    def update_image(self, image: Image.Image):
        self._update_queue.put(image)

    def _process_queue(self):
        if self._root and self._image_label:
            while not self._update_queue.empty():
                image = self._update_queue.get()
                self._image = ImageTk.PhotoImage(image, master=self._root)
                self._image_label.config(image=self._image)
                self._image_label.image = self._image
                self._root.maxsize(self._image.width(), self._image.height())
                self._root.minsize(self._image.width(), self._image.height())

            if not self._stop_flag.is_set():
                self._root.after(100, self._process_queue)
            else:
                self._root.quit()

    def run(self):
        self._root = tk.Tk()
        self._root.title(f"ST7789 {self._id}")
        self._image_label = tk.Label(self._root)
        self._image_label.pack()
        self._root.after(100, self._process_queue)
        self._root.mainloop()

    def stop(self):
        self._stop_flag.set()

