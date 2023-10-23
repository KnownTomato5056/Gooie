from Classes.widget import Widget
from Classes.image import surface_blur
from pygame.image import load
from Classes.image import blit_center
from Math.image_math import add_corners


class Button(Widget):
    def __init__(
        self,
        app,
        master,
        width: int = 80,
        height: int = 30,
        x: int = 0,
        y: int = 0,
        anchor: str = 1,
        command = None,
        resizeable = False,
        events: set = {'enter', 'leave', 'left_button_up'},
        image_path: str = None,
        blur = True,
        round_corners = None,
        ):

        super().__init__(app, master, events, width, height, x, y, anchor, resizeable)
        self.command = command
        self.blur = blur
        self.round_corners = round_corners

        self.image = load(image_path) if image_path else None

        self.init_surfaces()

    def init_surfaces(self):
        self.default_surface = surface_blur(self.background_surface, 5 if self.blur else 0, 0.85)
        self.hover_surface = surface_blur(self.background_surface, 10 if self.blur else 0, 0.75)

        if self.round_corners:
            self.default_surface = add_corners(self.default_surface, corners=self.round_corners)
            self.hover_surface = add_corners(self.hover_surface, corners=self.round_corners)

        if self.image:
            blit_center(self.default_surface, self.image)
            blit_center(self.hover_surface, self.image)

        self.update(surface=self.default_surface)

    def on_enter(self):
        self.update(surface=self.hover_surface)

    def on_leave(self):
        self.update(surface=self.default_surface)

    def on_left_button_up(self):
        if self.command: self.command()