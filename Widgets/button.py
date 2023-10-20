from Classes.widgets import Widget
from Classes.image import surface_blur


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
        events: set = {'enter', 'leave', 'left_button_up'},
        ):

        super().__init__(app, master, events, width, height, x, y, anchor)
        self.command = command
        self.init_surfaces()
        self.update(surface=self.default_surface)

    def init_surfaces(self):
        self.default_surface = surface_blur(self.background_surface, 5, 0.85)
        self.hover_surface = surface_blur(self.background_surface, 10, 0.75)

    def on_enter(self):
        self.update(surface=self.hover_surface)

    def on_leave(self):
        self.update(surface=self.default_surface)

    def on_left_button_up(self):
        if self.command: self.command()
        