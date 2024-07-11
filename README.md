# Python ST7789 Emulator

Python Library based on [Pimoroni ST7789 library](https://github.com/pimoroni/st7789-python/) to allow development of ST7789 displays using a GUI instead of connected hardware.

# Usage

If you have established code using the [Pimoroni ST7789 library](https://github.com/pimoroni/st7789-python/), then adding this library is as simple as updating your import to match the following:

```python
try:
    import st7789
except ImportError:
    import st7789_emulator as st7789
```

Once you run your code a window is generated for each instance of a ST7789 display which will show the image to scale of the configured display.