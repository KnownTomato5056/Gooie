from pygame.rect import Rect
from pygame.surface import Surface


class Widget:
    def __init__(self, app, master, events, width, height, dx, dy, anchor, resizeable):
        self.app = app
        self.master = master
        if type(self.master) != Surface: 
            self.master.children.add(self)

        self.events = events

        self.dx = dx
        self.dy = dy

        self.x = None
        self.y = None
        self.resizeable = resizeable
        self.anchor = anchor
        self.rect = None

        if resizeable:
            self.wf, self.hf = width, height
            self.width = width()
            self.height = height()
        else:
            self.width = width
            self.height = height

        self.place(dx, dy, anchor)

        self.active = True
        self.drag = False
        self.drag_pos = None

        self.background_surface = self.get_background_surface()
        self.default_surface = Surface((self.width, self.height))

        self.app.widgets.append(self)

    def get_background_surface(self):
        return self.master.subsurface(self.rect).copy()

    def place(self, x, y, anchor=1):
        if anchor == 1 or anchor == 'top_left':
            self.x, self.y = x, y

        elif anchor == 2 or anchor == 'top_right':
            self.x, self.y = self.master.get_width() - x, y

        elif anchor == 3 or anchor == 'bottom_right':
            self.x, self.y = self.master.get_height() - x, self.master.get_height() - y

        elif anchor == 4 or anchor == 'bottom_left':
            self.x, self.y = x, self.master.get_height() - y

        self.rect = Rect(self.x, self.y, self.width, self.height)

    def reindent(self):
        if self.resizeable:
            self.width = self.wf()
            self.height = self.hf()

        self.place(self.dx, self.dy, self.anchor)
        self.background_surface = self.get_background_surface()
        self.init_surfaces()
        self.master.blit(self.default_surface, self.rect)

    def update(self, surface=None, rect=None):
        if not rect: rect = self.rect
        if not surface: surface = self.default_surface
        self.master.blit(surface, rect)
        if type(self.master) == Surface:
            self.app.update_list.append(rect)
        else:
            self.master.child_update(rect)

    def init_surfaces(self):
        self.default_surface = Surface((self.width, self.height))

    def on_enter(self):
        pass

    def on_leave(self):
        pass

    def on_drag(self):
        pass

    def on_left_button_down(self):
        pass

    def on_left_button_up(self):
        pass

    def on_right_button_down(self):
        pass

    def on_right_button_up(self):
        pass

    def on_quit(self):
        pass