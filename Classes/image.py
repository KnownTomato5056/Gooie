from PIL import Image
from pygame.image import fromstring
from math import ceil


def normalize_size(current: tuple, expected: tuple):
    factor = max(expected[0] / current[0], expected[1] / current[1])
    return (ceil(current[0] * factor), ceil(current[1] * factor))


def convert_img(filepath: str, size: str):
    img = Image.open(filepath)
    img.thumbnail(normalize_size(img.size, size))
    return fromstring(img.tobytes(), img.size, img.mode).convert()

def surface_blur(surface):
    pass
