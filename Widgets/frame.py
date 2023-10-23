from Classes.widget import Widget
from Classes.image import surface_blur
from Widgets.label import Label


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
        self.children = set()

        self.init_surfaces()
        # This is the surface accessible to the children of this class
        self.update(surface=self.default_surface)
        

    def init_surfaces(self):
        self.default_surface = surface_blur(self.background_surface, radius=20, darken=0.7)
        

    def blit(self, source, rect):
        # To be accessed by children
        self.default_surface.blit(source, rect)

    def subsurface(self, rect):
        # To be accessed by children
        return self.background_surface.subsurface(rect)

    def child_update(self, rect):
        real_rect = rect.move(self.x, self.y)
        self.master.blit(self.default_surface, self.rect)
        self.app.update_list.append(real_rect)

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height
