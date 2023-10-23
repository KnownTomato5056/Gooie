from Classes.widget import Widget
from Classes.image import surface_blur, blit_center
from Math.image_math import add_corners
from pygame.font import SysFont
from pygame.image import load


class Label(Widget):
    def __init__(
        self,
        app,
        master,
        width: int = 80,
        height: int = 30,
        x: int = 0,
        y: int = 0,
        anchor: str = 1,
        events: set = {},
        text: str = None,
        font: str = 'Arial',
        font_size: int = 17,
        font_color: tuple = (255, 255, 255),
        resizeable: bool = False,
        image_path: str = None,
        blur: int = 5,
        darken: float = 0.85,
        round_corners: set = None,
    ):
        super().__init__(app, master, events, width, height, x, y, anchor, resizeable)
        self.blur = blur
        self.darken = darken
        self.image_surface = load(image_path) if image_path else None
        self.round_corners = round_corners
        self.text = text
        if self.text:
            self.font = SysFont(font, font_size)
            self.font_surface = self.font.render(self.text, True, font_color)
                
        self.init_surfaces()

    def init_surfaces(self):
        self.default_surface = surface_blur(self.background_surface, self.blur, self.darken)
        if self.text: blit_center(self.default_surface, self.text_surface)
        if self.image_surface: blit_center(self.default_surface, self.image_surface)
        if self.round_corners: self.default_surface = add_corners(self.default_surface, corners=self.round_corners)
        self.update(surface=self.default_surface)
