from pygame.rect import Rect
from pygame.surface import Surface


class Widget:
    def __init__(self, app, master, events, width, height, x, y, anchor):
        self.app = app
        self.master = master
        self.events = events

        self.x, self.y = 0, 0
        self.place(x, y, anchor)

        self.width, self.height = width, height

        self.active = True
        self.rect = Rect(self.x, self.y, self.width, self.height)
        self.surface = Surface((width, height))

        self.surface.set_alpha(30)
        

        self.app.widgets.add(self)
        self.update()

    def place(self, x, y, anchor=1):
        if anchor == 1 or anchor == 'top_left':
            self.x = x
            self.y = y
        elif anchor == 2 or anchor == 'top_right':
            self.x = self.app.width - x
            self.y = y
        elif anchor == 3 or anchor == 'bottom_right':
            self.x = self.app.width - x
            self.y = self.app.height - y
        elif anchor == 4 or anchor == 'bottom_left':
            self.x = x
            self.y = self.app.height - y

    def update(self, rect=None):
        if not rect: rect = self.rect
        self.master.blit(self.surface, self.rect)
        if type(self.master) == Surface:
            self.app.update_list.append(self.rect)
        else:
            self.master.update(rect)