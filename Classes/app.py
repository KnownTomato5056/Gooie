from Classes.image import convert_img
from Classes.eventhandler import EventHandler
from Widgets.button import Button
from pygame import init, display, event, NOFRAME
from pygame.time import Clock




class App:
    def __init__(self,
                 size: tuple[int, int] = (700, 700),
                 fps: int = 60,
                 bg_img_path: str = r'Assets/Backgrounds/bg1.jpg',
                 buttons: bool = True
        ):

        init()
        self.size = size
        self.width, self.height = self.size
        self.screen = display.set_mode(size, NOFRAME)
        self.clock = Clock()
        self.fps = fps
        self.buttons = buttons

        self.widgets = set()
        self.update_list = []

        self.bg_img = convert_img(bg_img_path, self.size)
        self.bg_rect = self.screen.blit(self.bg_img, (0, 0))

        if self.buttons: self.add_buttons()
        self.event_handler = EventHandler(self)


    def add_buttons(self):
        close_btn = Button(self, self.screen, width=50, height=30, x=50, y=0, anchor=2)
        self.widgets.add(close_btn)

    def update(self):
        display.update(self.update_list)
        self.update_list.clear()

    def run(self):
        display.flip()
        while True:
            self.clock.tick(self.fps)
            self.event_handler.handle(event.get())
            self.update()