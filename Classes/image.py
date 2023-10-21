from PIL import Image
from PIL.ImageFilter import BoxBlur
from PIL.ImageEnhance import Brightness
from pygame.image import fromstring, tobytes
from pygame.surface import Surface
from math import ceil


def normalize_size(current: tuple, expected: tuple):
    factor = max(expected[0] / current[0], expected[1] / current[1])
    return (ceil(current[0] * factor), ceil(current[1] * factor))


def convert_img(filepath: str, size: tuple):
    img = Image.open(filepath)
    img.thumbnail(normalize_size(img.size, size))
    img = img.crop([0, 0, size[0], size[1]])
    surf = fromstring(img.tobytes(), img.size, img.mode)
    return surf.convert_alpha()



def surface_blur(surface, radius=5, darken=1):
    size = surface.get_width(), surface.get_height()
    mode = 'RGBA'
    img = Image.frombytes(mode, size, tobytes(surface, mode))
    img = img.filter(BoxBlur(radius))
    img = Brightness(img).enhance(darken)
    return fromstring(img.tobytes(), size, mode)


def np_blur(surface, radius=5, darken=1):
    size = surface.shape[:2]