from pygame.rect import Rect
from pygame.surface import Surface


class Widget:
    def __init__(self, app, master, events, width, height, dx, dy, anchor):
        self.app = app
        self.master = master
        self.events = events

        self.dx = dx
        self.dy = dy

        self.x = None
        self.y = None
        self.anchor = anchor
        self.rect = None

        self.width = width
        self.height = height
        self.place(dx, dy, anchor)

        self.active = True

        self.background_surface = self.get_background_surface()
        self.default_surface = Surface((self.width, self.height))

        self.app.widgets.add(self)

    def get_background_surface(self):
        if type(self.master) == Surface:
            return self.master.subsurface(self.rect).copy()
        else:
            return self.master.surface.subsurface(self.rect).copy()

    def place(self, x, y, anchor=1):
        if anchor == 1 or anchor == 'top_left':
            self.x, self.y = x, y
            
        elif anchor == 2 or anchor == 'top_right':
            self.x, self.y = self.app.width - x, y
            
        elif anchor == 3 or anchor == 'bottom_right':
            self.x, self.y = self.app.width - x, self.app.height - y
             
        elif anchor == 4 or anchor == 'bottom_left':
            self.x, self.y = x, self.app.height - y

        self.rect = Rect(self.x, self.y, self.width, self.height)

    def reindent(self):
        self.place(self.dx, self.dy, self.anchor)
        self.default_surface = Surface((self.width, self.height))
        self.background_surface = self.get_background_surface()
        self.init_surfaces()
        self.master.blit(self.default_surface, self.rect)

    def update(self, rect=None, surface=None):
        if not rect: rect = self.rect
        if not surface: surface = self.default_surface
        self.master.blit(surface, rect)
        if type(self.master) == Surface:
            self.app.update_list.append(rect)
        else:
            self.master.update(rect)
            
    def init_surfaces(self):
        self.default_surface = Surface((self.width, self.height))