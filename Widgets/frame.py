from Classes.widgets import Widget
from Classes.image import surface_blur


class Frame(Widget):
    def __init__(
            self,
            app,
            master,
            width: int = 200,
            height: int = 200,
            x: int = 0,
            y: int = 0,
            anchor: str = 1,
            resizeable = False,
            events: set = {},
        ):

        super().__init__(app, master, events, width, height, x, y, anchor, resizeable)
        self.init_surfaces()
        self.update(surface=self.default_surface)

    def init_surfaces(self):
        self.default_surface = surface_blur(self.background_surface, radius=20, darken=0.7)
        
    def place():
        pass