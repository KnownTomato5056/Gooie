from Classes.widgets import Widget


class Button(Widget):
    def __init__(
        self,
        app,
        master,
        text: str = 'Button',
        width: int = 80,
        height: int = 30,
        x: int = 0,
        y: int = 0,
        anchor: str = 1,
        enter_color: str = 2,

        events: set = {'enter', 'leave', 'left_button_down',
                       'left_button_up'}):

        super().__init__(app, master, events, width, height, x, y, anchor)
        self.text = text

    def on_enter(self):
        print('enter')

    def on_leave(self):
        print('leave')

    def on_left_button_down(self):
        print('click')

    def on_left_button_up(self):
        print('lift')