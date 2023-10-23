from Classes.image import convert_img
from Classes.eventhandler import EventHandler
from Widgets.button import Button
from Widgets.titlebar import TitleBar
from pygame import display, event, quit, NOFRAME
from pygame.time import Clock
from pygame._sdl2.video import Window
from win32api import GetMonitorInfo, MonitorFromPoint


"""
Icons by:
icon by <a target="_blank" href="https://icons8.com">Icons8</a>
"""


def get_monitor_size():
    monitor_info = GetMonitorInfo(MonitorFromPoint((0,0)))
    work_area = monitor_info.get("Work")
    return work_area[2], work_area[3]


class App:
    def __init__(self,
                 size: tuple[int, int] = (700, 700),
                 fps: int = 60,
                 bg_img_path: str = r'Assets/Backgrounds/bg_9.jpg',
        ):
        self.size = size
        self.width, self.height = self.size
        self.screen = display.set_mode(size, NOFRAME)

        self.clock = Clock()
        self.fps = fps
        self.desktop_size = get_monitor_size()
        self.window = Window.from_display_module()

        self.widgets = []
        self.update_list = []

        self.bg_img_path = bg_img_path
        self.bg_img = convert_img(self.bg_img_path, self.size)
        self.bg_rect = self.screen.blit(self.bg_img, (0, 0))

        self.add_buttons()
        self.add_title_bar()

        self.event_handler = EventHandler(self)


    def add_buttons(self):
        close_btn = Button(self, self.screen, width=50, height=40, x=50, y=0, anchor=2, command=quit, image_path=r'Assets\Buttons\close_btn_0.png')
        win_btn = Button(self, self.screen, width=50, height=40, x=100, y=0, anchor=2, command=self.win_max_min, image_path=r'Assets\Buttons\maximize_btn_0.png')
        min_btn = Button(self, self.screen, width=50, height=40, x=150, y=0, anchor=2, command=self.minimize, image_path=r'Assets\Buttons\minimize_btn_0.png')

    def add_title_bar(self):
        title_bar = TitleBar(
            self, self.screen, width=lambda: self.width-150, height=lambda: 40, x=0, y=0, anchor=1, resizeable=True
        )

    def win_max_min(self, spawn=(200, 100)):
        if not self.is_maximized():
            self.size = self.desktop_size[0], self.desktop_size[1] - 1
            self.window.position = 0, 0
            self.screen = display.set_mode(self.size, NOFRAME)
        else:
            self.size = 700, 700
            self.window.position = spawn
            self.screen = display.set_mode(self.size, NOFRAME)

        self.width, self.height = self.size
        self.bg_img = convert_img(self.bg_img_path, self.size)
        self.bg_rect = self.screen.blit(self.bg_img, (0, 0))
        self.reindent()

    def minimize(self):
        display.iconify()

    def restore(self):
        display.flip()

    def reindent(self):
        for widget in self.widgets: widget.reindent()
        display.flip()

    def update(self):
        display.update(self.update_list)
        self.update_list.clear()
        
    def is_maximized(self):
        return not self.size[0] < self.desktop_size[0]

    def run(self):
        display.flip()
        while 1:
            self.clock.tick(self.fps)
            self.event_handler.handle(event.get())
            self.update()