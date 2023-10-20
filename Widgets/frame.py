from Classes.widgets import Widget


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
            events: set = {},
        ):
        
        super().__init__(app, master, events, width, height, x, y, anchor)
        
        