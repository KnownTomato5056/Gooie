from Widgets.frame import Frame
from Widgets.label import Label
from time import time


class TitleBar(Frame):
    def __init__(self, *args, **kwargs):
        kwargs['events'] = {'drag'}
        super().__init__(*args, **kwargs)

        self.time = time()
        self.image_path = r"Assets\logo3.png"
        
        self.title_label = Label(
            self.app,
            self,
            width=100,
            height=40,
            x=0,
            y=0,
            anchor=1,
            blur=5,
            darken=0.6,
            image_path=self.image_path,
        )

    def on_drag(self, event):
        pos = event.dict['pos']
        pos2 = self.app.window.position
        if pos2[1] < 1:
            self.app.win_max_min()
            self.drag = False
            return
        self.app.window.position = pos[0] + pos2[0] - self.drag_pos[0], pos[1] + pos2[1] -self.drag_pos[1]