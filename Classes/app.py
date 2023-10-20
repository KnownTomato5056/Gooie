from Classes.image import convert_img
from Classes.eventhandler import EventHandler
from Widgets.button import Button
from pygame import init, display, event, quit, NOFRAME
from pygame._sdl2.video import Window
from win32api import GetMonitorInfo, MonitorFromPoint
from pygame.time import Clock
from sys import exit



def get_monitor_size():
    monitor_info = GetMonitorInfo(MonitorFromPoint((0,0)))
    work_area = monitor_info.get("Work")
    return work_area[2], work_area[3]

class App:
    def __init__(self,
                 size: tuple[int, int] = (700, 700),
                 fps: int = 60,
                 bg_img_path: str = r'Assets/Backgrounds/bg2.jpg',
                 buttons: bool = True
        ):

        init()
        self.size = size
        self.width, self.height = self.size
        self.screen = display.set_mode(size, NOFRAME)
        self.clock = Clock()
        self.fps = fps
        self.buttons = buttons
        self.desktop_size = get_monitor_size()
        self.window = Window.from_display_module()

        self.widgets = set()
        self.update_list = []

        self.bg_img_path = bg_img_path
        self.bg_img = convert_img(self.bg_img_path, self.size)
        self.bg_rect = self.screen.blit(self.bg_img, (0, 0))

        if self.buttons: self.add_buttons()
        self.event_handler = EventHandler(self)


    def add_buttons(self):
        close_btn = Button(self, self.screen, width=50, height=40, x=50, y=0, anchor=2, command=quit)
        win_btn = Button(self, self.screen, width=50, height=40, x=100, y=0, anchor=2, command=self.win_max_min)


    def win_max_min(self):
        print(self.size, self.desktop_size)
        if self.size[0] < self.desktop_size[0]:
            self.size = self.desktop_size[0], self.desktop_size[1] - 1
            self.window.position = 0, 0
            self.screen = display.set_mode(self.size, NOFRAME)
        else:
            self.size = 700, 700
            self.window.position = 200, 100
            self.screen = display.set_mode(self.size, NOFRAME)
            
        self.width, self.height = self.size
        self.bg_img = convert_img(self.bg_img_path, self.size)
        self.bg_rect = self.screen.blit(self.bg_img, (0, 0))
        self.reindent()

    def reindent(self):
        for widget in self.widgets: widget.reindent()
        display.flip()

    def update(self):
        display.update(self.update_list)
        self.update_list.clear()

    def run(self):
        display.flip()
        while 1:
            self.clock.tick(self.fps)
            self.event_handler.handle(event.get())
            self.update()