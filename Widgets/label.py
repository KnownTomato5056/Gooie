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
        resizeable=False,
        events: set = {},
        text: str = None,
        image_path: str = None,
        blur=5,
        darken=0.85,
        round_corners=None,
    ):
        super().__init__(app, master, events, width, height, x, y, anchor, resizeable)
        self.text = text
        if text:
            self.font = SysFont('Arial', 17)
            self.render_text()

        self.blur = blur
        self.darken = darken
        self.image_path = image_path
        self.round_corners = round_corners
        self.init_surfaces()

    def render_text(self):
        self.text_surface =  self.font.render(self.text, True, (255, 255, 255), None)

    def init_surfaces(self):
        self.default_surface = surface_blur(self.background_surface, self.blur, self.darken)
        self.update(surface=self.default_surface)

        if self.text:
            blit_center(self.default_surface, self.text_surface)
            
        if self.image_path:
            self.image = load(self.image_path)
            blit_center(self.default_surface, self.image)

        if self.round_corners:
            self.default_surface = add_corners(self.default_surface, corners=self.round_corners)
            
        self.update(surface=self.default_surface)
