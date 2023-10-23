import sys
from Classes.widget import Widget
from Classes.image import surface_blur
from pygame.image import load
from pygame.font import SysFont
from Classes.image import blit_center
from Math.image_math import add_corners


class Button(Widget):
    def __init__(
        self,
        app,
        master,
        x: int = 0,
        y: int = 0,
        width: int = 80,
        height: int = 30,
        anchor: str = 1,
        events: set = {'enter', 'leave', 'left_button_up'},
        command: callable = None,
        image_path: str = None,
        text: str = None,
        font: str = 'Arial',
        font_size: int = 17,
        font_color: tuple = (255, 255, 255),
        resizeable: bool = False,
        default_blur: bool = 5,
        hover_blur: bool = 10,
        round_corners: set = None,
        default_darken: float = 0.85,
        hover_darken: float = 0.75,
    ):

        super().__init__(app, master, events, width, height, x, y, anchor, resizeable)
        self.command = command
        self.round_corners = round_corners
        self.default_blur = default_blur
        self.hover_blur = hover_blur
        self.default_darken = default_darken
        self.hover_darken = hover_darken
        self.image = load(image_path) if image_path else None

        self.text = text
        if self.text:
            self.font = SysFont(font, font_size)
            self.font_surface = self.font.render(self.text, True, font_color)

        self.init_surfaces()

    def init_surfaces(self):
        self.default_surface = surface_blur(self.background_surface, self.default_blur, self.default_darken)
        self.hover_surface = surface_blur(self.background_surface, self.hover_blur, self.hover_darken)

        if self.round_corners:
            self.default_surface = add_corners(self.default_surface, corners=self.round_corners)
            self.hover_surface = add_corners(self.hover_surface, corners=self.round_corners)

        if self.image:
            blit_center(self.default_surface, self.image)
            blit_center(self.hover_surface, self.image)

        if self.text:
            blit_center(self.default_surface, self.font_surface)
            blit_center(self.hover_surface, self.font_surface)

        self.update(surface=self.default_surface)

    def on_enter(self):
        self.update(surface=self.hover_surface)

    def on_leave(self):
        self.update(surface=self.default_surface)

    def on_left_button_up(self):
        if self.command: self.command()