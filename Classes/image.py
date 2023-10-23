from PIL import Image
from PIL.ImageFilter import BoxBlur
from PIL.ImageEnhance import Brightness
from pygame.image import fromstring, tobytes

from pygame.image import load
from pygame.transform import smoothscale_by


def normalize_factor(current: tuple, expected: tuple):
    return  max(expected[0] / current[0], expected[1] / current[1])


def convert_img(filepath: str, size: tuple):
    img = load(filepath)
    factor = normalize_factor(img.get_size(), size)
    return smoothscale_by(img, factor)


def surface_blur(surface, radius=5, darken=1):
    size = surface.get_width(), surface.get_height()
    mode = 'RGBA'
    img = Image.frombytes(mode, size, tobytes(surface, mode))
    img = img.filter(BoxBlur(radius))
    img = Brightness(img).enhance(darken)
    return fromstring(img.tobytes(), size, mode)


def blit_center(master, surface):
    coord = master.get_width() / 2, master.get_height() / 2
    master.blit(surface, surface.get_rect(center=coord))